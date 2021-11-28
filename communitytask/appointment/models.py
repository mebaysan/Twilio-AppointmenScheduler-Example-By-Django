from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz
from communitytask.settings import TIME_ZONE
from django.template.defaultfilters import slugify
# Create your models here.


class AppointmentAccount(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=False, blank=False, related_name='appointment_account')
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Appointment Account'
        verbose_name_plural = 'Appointment Accounts'


class Appointment(models.Model):
    account = models.ForeignKey(
        AppointmentAccount, on_delete=models.CASCADE, related_name='appointment')
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    appointment_datetime = models.DateTimeField(
        null=False, blank=False, auto_created=True, editable=True)
    scheduler_id = models.TextField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.scheduler_id = slugify(
            f"{self.account.user.username}{self.account.phone_number}{self.appointment_datetime}{self.title}")
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    @property
    def get_sms_content(self):
        if not self.content:
            return f"Appointment: {self. title}"
        else:
            return f"Appointment: {self.title}\nDetail: {self.content}"

    @property
    def get_date_time(self):
        """Returns the casted server's timezone

        Returns:
            datetime: prepared `appointment_object.appointment_datetime` to schedule jobs
        """
        casted_tz = self.appointment_datetime.astimezone(
            pytz.timezone(TIME_ZONE))
        return datetime(casted_tz.year, casted_tz.month,
                        casted_tz.day, casted_tz.hour, casted_tz.minute)

    @classmethod
    def get_next_schedules(cls):
        """Returns the next schedules

        Returns:
            list: list of Appointment objects
        """
        return Appointment.objects.filter(appointment_datetime__gte=datetime.now(tz=pytz.timezone(TIME_ZONE)))

    @classmethod
    def get_scheduled_appointment(cls, job_id):
        return cls.objects.filter(scheduler_id=job_id).first()
