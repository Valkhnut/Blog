from django.db import models

from django.utils import timezone


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
        verbose_name='Content'
    )

    publish = models.DateTimeField(
        default=timezone.now,
        verbose_name='Published date'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created date'
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated date'
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(
                fields=['-publish']
            )
        ]

    def __str__(self):
        return self.title
