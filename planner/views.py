from django.shortcuts import render
from django.views import generic

from planner.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")

    class Meta:
        ordering = ["is_completed", "-datetime"]
