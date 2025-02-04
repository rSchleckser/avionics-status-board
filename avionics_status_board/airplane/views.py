from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Airplane
from work.models import Work
from django.urls import reverse_lazy

class AirplaneListView(ListView):
    model = Airplane
    template_name = "airplane/airplane_list.html"
    context_object_name = "airplanes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Status overview data
        context["planes"] = Airplane.objects.count()
        context["deliveries"] = Airplane.objects.filter(delivered=True).count()
        context["ticket"] = Airplane.objects.filter(ticketed=True).count()
        context["inWork"] = Work.objects.filter(status="in_progress").count()
        context["cantWork"] = Work.objects.filter(status="cant_work").count()
        context["openPaper"] = Work.objects.filter(status="open_paper").count()

        return context

class AirplaneDetailView(DetailView):
    model = Airplane
    template_name = "airplane/airplane_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_items"] = Work.objects.filter(airplane=self.object)  # Fetch jobs for this airplane
        return context

class WorkCreateView(CreateView):
    model = Work
    fields = ["name", "description", "type", "status", "assigned_to"]
    template_name = "work/work_form.html"

    def form_valid(self, form):
        airplane = get_object_or_404(Airplane, pk=self.kwargs["pk"])  # Get airplane from URL
        form.instance.airplane = airplane  # Assign job to the airplane
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("airplane:detail", kwargs={"pk": self.kwargs["pk"]})  # Redirect back to airplane details

class AirplaneCreateView(CreateView):
    model = Airplane
    fields = ["line_number", "location_city", "location_stall", "effectivity", "customer", "delivered", "ticketed"]
    template_name = "airplane/airplane_form.html"
    success_url = reverse_lazy("airplane:list")

class AirplaneUpdateView(UpdateView):
    model = Airplane
    fields = ["line_number", "location_city", "location_stall", "effectivity", "customer", "delivered", "ticketed"]
    template_name = "airplane/airplane_form.html"
    success_url = reverse_lazy("airplane:list")
