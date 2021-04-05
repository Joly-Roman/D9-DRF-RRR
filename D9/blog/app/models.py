from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', blank=True,null=True, related_name='posts', on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'