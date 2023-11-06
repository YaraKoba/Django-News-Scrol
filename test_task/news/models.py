from django.db import models
from django.contrib.auth.models import User
from datetime import  datetime

from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=5000)
    img = models.ImageField(null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.now)
    
    views = models.BigIntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    user = models.ForeignKey(User, related_name='news', on_delete=models.CASCADE, default=None)
    tag = models.ManyToManyField(Tag, related_name='news', blank=True)

    def __str__(self):
        return f'{self.title}'
