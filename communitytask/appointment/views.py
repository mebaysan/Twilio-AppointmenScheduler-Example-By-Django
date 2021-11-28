from django.shortcuts import render, HttpResponse
from baysantwilio.models import TwilioInterface
from communitytask.settings import SCHEDULER
# Create your views here.


def index(request):
    print(SCHEDULER.get_jobs())
    return HttpResponse('HELLO')
