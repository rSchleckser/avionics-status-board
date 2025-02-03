from django.urls import path
from .views import (
    WorkListView, WorkCreateView, WorkEditView, WorkArchiveView, WorkScheduleView, status_dashboard
)

app_name ="work"

urlpatterns = [
    path('', WorkListView.as_view(), name='work-list'),
    path('create/', WorkCreateView.as_view(), name='work-create'),
    path('<int:pk>/edit/', WorkEditView.as_view(), name='work-edit'),
    path('<int:pk>/archive/', WorkArchiveView.as_view(), name='work-archive'),
    path('schedule/', WorkScheduleView.as_view(), name='work-schedule'),
    path("status-dashboard/", status_dashboard, name="status-dashboard"),
]
