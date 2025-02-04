from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Work, Airplane

from django.views.generic import ListView
from .models import Work

class WorkListView(ListView):
    model = Work
    template_name = "work/work_list.html"
    context_object_name = "work_items" 


class WorkDetailView(DetailView):
    model = Work
    template_name = "work/work_detail.html"

class WorkCreateView(LoginRequiredMixin, CreateView):
    model = Work
    fields = ['name', 'description', 'type', 'status', 'assigned_to']  # Fixed field name
    template_name = 'work/work_form.html'
    success_url = reverse_lazy('work-list')  # Ensure this matches `urls.py`

class WorkEditView(LoginRequiredMixin, UpdateView):
    model = Work
    fields = ['name', 'status', 'assigned_to']  # Fixed field name
    template_name = 'work/work_form.html'
    success_url = reverse_lazy('work-list')

class WorkArchiveView(LoginRequiredMixin, UpdateView):
    model = Work
    fields = ['status']
    template_name = 'work/work_archive.html'
    success_url = reverse_lazy('work-list')

class WorkScheduleView(LoginRequiredMixin, ListView):  # Changed to ListView
    model = Work
    template_name = 'work/work_schedule.html'
    context_object_name = 'scheduled_work'

    def get_queryset(self):
        return Work.objects.filter(status="scheduled")  # Adjust filter as needed


def status_overview(request):
    airplanes = Airplane.objects.all()
    work_items = Work.objects.all()

    context = {
        "planes": airplanes.count(),
        "deliveries": airplanes.filter(delivered=True).count(),
        "ticket": airplanes.filter(ticketed=True).count(),
        "inWork": work_items.filter(status="in_progress").count(),
        "cantWork": work_items.filter(status="cant_work").count(),
        "openPaper": work_items.filter(status="open_paper").count(),
        "airplanes": airplanes,
        "work_items": work_items,
    }
    return render(request, "work/status_overview.html", context)
