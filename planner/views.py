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


class TaskUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("planner:index")
    form_class = TaskCreationForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("planner:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("planner:tag-list")
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("planner:tag-list")
    fields = "__all__"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("planner:tag-list")
