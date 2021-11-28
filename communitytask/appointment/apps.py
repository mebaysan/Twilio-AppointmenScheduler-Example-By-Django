from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment'

    def ready(self):
        """
        we should import the signals in here.
        """
        # Import signals
        from appointment import signals

        # Schedule appointmens for sending sms
        from baysantwilio.models import TwilioInterface
        TwilioInterface.schedule_appointments()