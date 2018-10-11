from django.shortcuts import render
from .models import Timesheet

def index(request):
    timesheet_list = Timesheet.objects.all()
    context = {'timesheet_list' : timesheet_list}
    return render(request, 'timesheetApp/index.html', context)