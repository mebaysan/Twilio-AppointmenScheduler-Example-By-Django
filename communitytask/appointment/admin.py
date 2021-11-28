from django.contrib import admin
from .models import AppointmentAccount, Appointment
# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ['scheduler_id']


admin.site.register(AppointmentAccount)
admin.site.register(Appointment,AppointmentAdmin)
