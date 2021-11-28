from .models import AppointmentAccount, Appointment
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from baysantwilio.models import TwilioInterface
import pytz
from communitytask.settings import SCHEDULER,TIME_ZONE


@receiver(post_save, sender=User)
def create_user_appointment_account(sender, instance, **kwargs):
    """
    if the user (instance) hasn't an AppointmentAccount, an account will be created for the user.
    """
    if AppointmentAccount.objects.filter(user=instance).first() == None:
        AppointmentAccount.objects.create(user=instance).save()


@receiver(post_save, sender=Appointment)
def schedule_appointment(sender, instance, **kwargs):
    if SCHEDULER.get_job(instance.scheduler_id):  # update the time of appointment
        SCHEDULER.remove_job(instance.scheduler_id)
    SCHEDULER.add_job(TwilioInterface.send_message, 'date', run_date=instance.get_date_time, args=[
        instance.account.phone_number,  # we can not use not verified number.
        instance.get_sms_content], timezone=pytz.timezone(TIME_ZONE), id=instance.scheduler_id)


@receiver(post_delete, sender=Appointment)
def remove_scheduled_appointment(sender, instance, **kwargs):
    if SCHEDULER.get_job(instance.scheduler_id):  # remove the scheduled job
        SCHEDULER.remove_job(instance.scheduler_id)
