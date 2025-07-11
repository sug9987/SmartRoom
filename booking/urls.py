from django.urls import include, path
from . import views
from .views import (
    register, custom_login, custom_logout,
    home, admin_dashboard,
    edit_room, delete_room
)

urlpatterns = [
    # 🌐 Public pages
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),

    # 🔐 Authentication
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', register, name='register'),

    # 👤 User dashboard and features
    path('home/', home, name='home'),  # ✅ changed from user_dashboard to home
    path('rooms/', views.room_list, name='room_list'),
    path('book/', views.book_room, name='book_room'),
    path('history/', views.booking_history, name='booking_history'),

    # 🛠 Admin dashboard
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    # 🛠 Admin: Room management
    path('room/<int:room_id>/edit/', edit_room, name='edit_room'),
    path('room/<int:room_id>/delete/', delete_room, name='delete_room'),

    path('booked/<int:booking_id>/', views.booked_success, name='booked_success'),  # 👈 new route
    path('rooms/', views.rooms_page, name='rooms_page'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),

    path('add-room/', views.add_room, name='add_room'),

    path('admin/add-room/', views.add_room, name='add_room'),

     path('add-room/', views.add_room, name='add_room'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

]
