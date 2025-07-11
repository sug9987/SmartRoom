from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'

# booking/apps.py
def ready(self):
    import booking.signals  # type: ignore # If signals are in separate file
