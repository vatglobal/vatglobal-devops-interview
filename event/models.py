# models.py
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
