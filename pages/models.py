from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=150)
    time = models.TimeField()

    def __str__(self):
        return self.name