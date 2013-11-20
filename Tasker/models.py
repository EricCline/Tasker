from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField('due date')
    complete = models.BooleanField(default=False)
