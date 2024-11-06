from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To do'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    ]
    discription = models.TextField()
    title = models.CharField(max_length=250)
    due_time = models.DateTimeField(verbose_name=('due_time'), null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20, choices=[
        ('low','Low'),
        ('medium','Medium'),
        ('high', 'High'),
    ], default='medium')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

def __sts__(self):
    return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



