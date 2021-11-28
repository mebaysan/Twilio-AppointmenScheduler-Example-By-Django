from django.db import models
from twilio.rest import Client
from communitytask.settings import TWILIO_AUTH_TOKEN, TWILIO_SID, TWILIO_VERIFIED_PHONE_NUMBER,TWILIO_SENDER_PHONE_NUMBER,SCHEDULER,TIME_ZONE
from appointment.models import Appointment
import pytz
# Create your models here.


class TwilioInterface:
    """
    This class just an interface class, isn't a model class
    """
    SID = TWILIO_SID
    AUTH_TOKEN = TWILIO_AUTH_TOKEN
    FROM_NUMBER = TWILIO_SENDER_PHONE_NUMBER # We get this number from Twilio

    @classmethod
    def get_client(cls):
        """
        Returns a Twilio Client
        """
        return Client(cls.SID, cls.AUTH_TOKEN)

    @classmethod
    def send_message(cls, to_number=TWILIO_VERIFIED_PHONE_NUMBER,message_body='Hi there!'):
        """Send sms to number

        Args:
            to_number (str, optional): Target number. Defaults to TWILIO_VERIFIED_PHONE_NUMBER.
            message_body (str, optional): The sms content.

        Raises:
            SystemError: If there are any error to send message, the function will raise en error

        Returns:
            bool: If the sms was sent, returns True
        """
        client = cls.get_client()
        try:
            message = client.messages.create(
                body=message_body,
                from_=cls.FROM_NUMBER,
                to=to_number
            )
        except:
            raise SystemError(
                "We couldn't send the sms. Please check your Twilio credentials.")

        return True

    @classmethod
    def schedule_appointments(cls):
        """
        Schedule jobs for appointments which has greater datetime than now
        """
        for appointment in Appointment.get_next_schedules():
            SCHEDULER.add_job(cls.send_message, 'date', run_date=appointment.get_date_time, args=[
                appointment.account.phone_number,  # we can not use not verified number.
                appointment.get_sms_content], timezone=pytz.timezone(TIME_ZONE), id=appointment.get_scheduler_id)
