from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Airplane
from django.urls import reverse_lazy

class AirplaneListView(ListView):
    model = Airplane
    template_name = "airplane/airplane_list.html"
    context_object_name = "airplanes"

class AirplaneDetailView(DetailView):
    model = Airplane
    template_name = "airplane/airplane_detail.html"

class AirplaneCreateView(CreateView):
    model = Airplane
    fields = ["line_number", "effectivity", "customer", "delivered", "ticketed"]
    template_name = "airplane/airplane_form.html"
    success_url = reverse_lazy("airplane:list")

class AirplaneUpdateView(UpdateView):
    model = Airplane
    fields = ["line_number", "effectivity", "customer", "delivered", "ticketed"]
    template_name = "airplane/airplane_form.html"
    success_url = reverse_lazy("airplane:list")
