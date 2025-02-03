from django.urls import path
from .views import AirplaneListView, AirplaneDetailView, AirplaneCreateView, AirplaneUpdateView

app_name = "airplane"

urlpatterns = [
    path("", AirplaneListView.as_view(), name="list"),
    path("<int:pk>/", AirplaneDetailView.as_view(), name="detail"),
    path("create/", AirplaneCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", AirplaneUpdateView.as_view(), name="edit"),
]
