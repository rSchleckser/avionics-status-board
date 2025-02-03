from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Work, Airplane

class WorkListView(LoginRequiredMixin, ListView):
    model = Work
    template_name = 'work/work_list.html'
    context_object_name = 'work_items'

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

def status_dashboard(request):
    context = {
        "planes": Airplane.objects.count(),
        "deliveries": Airplane.objects.filter(delivered=True).count(),
        "ticket": Airplane.objects.filter(ticketed=True).count(),
        "inWork": Work.objects.filter(status="in_progress").count(),
        "cantWork": Work.objects.filter(status="cant_work").count(),
        "openPaper": Work.objects.filter(status="open_paper").count(),
    }
    return render(request, "work/status_dashboard.html", context)