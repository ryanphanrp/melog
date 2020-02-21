from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('story')
