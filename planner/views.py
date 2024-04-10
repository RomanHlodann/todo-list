from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from planner.forms import TaskCreationForm
from planner.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")

    class Meta:
        ordering = ["is_completed", "-datetime"]


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("planner:index")
    form_class = TaskCreationForm

