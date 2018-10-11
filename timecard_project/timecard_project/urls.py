from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('timesheet/', include('timesheetApp.urls')),
    path('admin/', admin.site.urls),
]