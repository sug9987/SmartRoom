from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.utils import timezone

# -------------------------------
# User Profile: Role Management
# -------------------------------
# class UserProfile(models.Model):
#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('employee', 'Employee'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

#     def __str__(self):
#         return f"{self.user.username} - {self.role}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=(('employee', 'Employee'), ('admin', 'Admin')), default='employee')

    def __str__(self):
        return self.user.username

# Automatically create a UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# -------------------------------
# Room Model: Meeting Rooms
# -------------------------------
class Room(models.Model):
    name = models.CharField(max_length=100)              # Room name (e.g., "2 BHK")
    location = models.CharField(max_length=100)          # Room location (e.g., "2nd Floor")
    capacity = models.PositiveIntegerField()             # Max people
    amenities = models.TextField()                       # E.g., "Projector, Whiteboard, AC"
    room_image_url = models.URLField(blank=True, null=True)  # ✅ Add this line!
    def __str__(self):
        return f"{self.name} ({self.location})"

# -------------------------------
# Booking Model: Reservations
# -------------------------------
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    purpose = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room.name} | {self.date} ({self.start_time}-{self.end_time}) by {self.user.username}"

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['room', 'date', 'start_time', 'end_time'],
                name='unique_room_booking'
            )
        ]

    @property
    def duration(self):
        """Returns the duration as a timedelta object"""
        start = datetime.combine(self.date, self.start_time)
        end = datetime.combine(self.date, self.end_time)
        return end - start

    @property
    def is_past(self):
        """Returns True if this booking is in the past"""
        now = timezone.now()
        booking_end = datetime.combine(self.date, self.end_time)
        return booking_end < now


