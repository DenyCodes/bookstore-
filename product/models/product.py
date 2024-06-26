from django.db import models

from product.models import Category

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)