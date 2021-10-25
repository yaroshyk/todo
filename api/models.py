from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    group = models.TextField(default='home')
    user_id = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.title
