from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Title'
    )

    slug = models.SlugField(
        max_length=250,
        verbose_name='SLUG'
    )

    body = models.TextField(

    )

    def __str__(self):
        return self.title