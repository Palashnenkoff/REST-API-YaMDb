from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='category name',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='category slug',
        max_length=50,
        unique=True
    )
