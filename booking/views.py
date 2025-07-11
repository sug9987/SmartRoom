from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from django.db.models import Q
from django.core.mail import send_mail
from django.db import IntegrityError

from .models import Room, Booking, UserProfile
from .forms import RegisterForm, CustomLoginForm, BookingForm, RoomForm

# ==================== AUTHENTICATION ====================

def custom_login(request):
    form = CustomLoginForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard' if user.is_staff else 'home')
        messages.error(request, "Invalid credentials")
    return render(request, 'booking/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                if User.objects.filter(username=user.username).exists():
                    messages.error(request, "⚠️ Username already taken.")
                    return render(request, 'booking/register.html', {'form': form})
                if User.objects.filter(email=user.email).exists():
                    messages.error(request, "⚠️ Email already registered.")
                    return render(request, 'booking/register.html', {'form': form})
                user.save()
                UserProfile.objects.get_or_create(user=user, role='employee')
                send_mail(
                    subject='✅ SmartRooms: Registration Successful',
                    message=(
                        f"Hi {user.username},\n\n"
                        f"Welcome to SmartRooms!\n\n"
                        f"You have successfully registered with your email: {user.email}.\n\n"
                        f"Regards,\nSmartRooms Team"
                    ),
                    from_email='noreply@smartrooms.com',
                    recipient_list=[user.email],
                    fail_silently=True
                )
                messages.success(request, "✅ Registration successful! Please log in.")
                return redirect('landing')
            except Exception as e:
                messages.error(request, f"❌ Error during registration: {str(e)}")
        else:
            messages.error(request, "❌ Please correct the errors in the form.")
    else:
        form = RegisterForm()
    return render(request, 'booking/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('landing')


# ==================== USER DASHBOARD ====================

@login_required
def home(request):
    today = timezone.now().date()
    user_id = request.user.id
    context = {
        'total_bookings': Booking.objects.filter(user_id=user_id).count(),
        'todays_bookings': Booking.objects.filter(user_id=user_id, date=today).count(),
        'upcoming_bookings': Booking.objects.filter(user_id=user_id, date__gt=today).count(),
    }
    return render(request, 'booking/home.html', context)


# ==================== ADMIN DASHBOARD ====================

@user_passes_test(lambda u: u.is_authenticated and u.is_staff)
def admin_dashboard(request):
    users = User.objects.all()
    rooms = Room.objects.all()
    bookings = Booking.objects.all()
    context = {
        'users': users,
        'rooms': rooms,
        'bookings': bookings,
        'total_users': users.count(),
        'total_rooms': rooms.count(),
        'total_bookings': bookings.count(),
    }
    return render(request, 'booking/admin_dashboard.html', context)


# ==================== ROOM BROWSING & BOOKING ====================

@login_required
def room_list(request):
    query = request.GET.get('q', '')
    rooms = Room.objects.all()
    if query:
        filters = Q(name__icontains=query) | Q(location__icontains=query) | Q(amenities__icontains=query)
        if query.isdigit():
            filters |= Q(capacity=int(query))
        rooms = rooms.filter(filters)
    return render(request, 'booking/room_list.html', {'rooms': rooms, 'query': query})


@login_required
def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            conflict = Booking.objects.filter(
                room=booking.room,
                date=booking.date,
                start_time__lt=booking.end_time,
                end_time__gt=booking.start_time
            )
            if conflict.exists():
                messages.error(request, "❌ This room is already booked at that time.")
            else:
                booking.save()
                messages.success(request, "✅ Booking confirmed!")
                send_mail(
                    subject='📅 SmartRooms: Booking Confirmed',
                    message=(
                        f"Hi {request.user.username},\n\n"
                        f"Your booking for '{booking.room.name}' is confirmed.\n"
                        f"📍 {booking.room.location} | 🗓 {booking.date} | ⏰ {booking.start_time} - {booking.end_time}\n\n"
                        f"Thank you for using SmartRooms!"
                    ),
                    from_email=None,
                    recipient_list=[request.user.email],
                    fail_silently=True
                )
                return redirect('booked_success', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})


@login_required
def booked_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'booking/booked_success.html', {'booking': booking})


@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-start_time')
    return render(request, 'booking/booking_history.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "❌ Booking has been cancelled.")
        send_mail(
            subject='🗑️ SmartRooms: Booking Cancelled',
            message=(
                f"Hi {request.user.username},\n\n"
                f"Your booking for '{booking.room.name}' on {booking.date} from {booking.start_time} to {booking.end_time} has been cancelled.\n\n"
                f"SmartRooms Team"
            ),
            from_email=None,
            recipient_list=[request.user.email],
            fail_silently=True
        )
        return redirect('booking_history')
    return render(request, 'booking/confirm_cancel.html', {'booking': booking})


# ==================== ADMIN ROOM MANAGEMENT ====================

@user_passes_test(lambda u: u.is_authenticated and u.is_staff)
def add_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        location = request.POST.get('location')
        description = request.POST.get('description')

        Room.objects.create(
            name=name,
            capacity=capacity,
            location=location,
            description=description
        )
        return redirect('admin_dashboard')

    return render(request, 'booking/add_room.html')


@user_passes_test(lambda u: u.is_authenticated and u.is_staff)
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "Room updated successfully.")
            return redirect('admin_dashboard')
    else:
        form = RoomForm(instance=room)
    return render(request, 'booking/edit_room.html', {'form': form, 'room': room})


@user_passes_test(lambda u: u.is_authenticated and u.is_staff)
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        messages.success(request, "Room deleted successfully.")
        return redirect('admin_dashboard')
    return render(request, 'booking/confirm_delete.html', {'room': room})


# ==================== STATIC PAGES ====================

def landing(request):
    rooms = Room.objects.all()
    return render(request, 'booking/landing.html', {'rooms': rooms})


def about(request):
    return render(request, 'booking/about.html')


def rooms_page(request):
    rooms = Room.objects.all()
    return render(request, 'booking/rooms.html', {'rooms': rooms})
