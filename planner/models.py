from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self) -> str:
        return f"{self.content}. Is completed: {self.is_completed}."


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
