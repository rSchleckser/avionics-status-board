from django.urls import path
from .views import AirplaneListView, AirplaneDetailView, AirplaneCreateView, AirplaneUpdateView, WorkCreateView

app_name = "airplane"

urlpatterns = [
    path("", AirplaneListView.as_view(), name="list"),
    path("<int:pk>/", AirplaneDetailView.as_view(), name="detail"),
    path("<int:pk>/add-work/", WorkCreateView.as_view(), name="add-work"),
    path("create/", AirplaneCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", AirplaneUpdateView.as_view(), name="edit"),
]
