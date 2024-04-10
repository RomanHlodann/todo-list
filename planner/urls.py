from django.urls import path

from planner.views import TaskListView


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
]

app_name = "planner"
