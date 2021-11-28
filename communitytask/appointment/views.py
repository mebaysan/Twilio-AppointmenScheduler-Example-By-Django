from django.shortcuts import HttpResponse
from communitytask.settings import SCHEDULER
from appointment.models import Appointment
# Create your views here.


def index(request):
    html = "<h1>You can see the scheduled jobs the following:</h1>"
    html += "<table>"
    html += "<tr> <th>Appointment</th> <th>User</th> <th>Appointment Date</th> <th>Job ID</th>"
    for i in SCHEDULER.get_jobs():
        job = Appointment.get_scheduled_appointment(i.id)
        html += f"<tr> <td>{job.title}</td> <td>{job.account.user}</td> <td>{job.get_date_time}</td> <td>{job.scheduler_id}</td> </tr>"
    html += "</table>"
    return HttpResponse(html)
