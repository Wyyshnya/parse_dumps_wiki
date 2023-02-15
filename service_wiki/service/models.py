from datetime import datetime, timedelta, date
from django.contrib.postgres.fields import ArrayField
from django.db import models
from .managers import ContentManager, CategoryManager, CategoryContentManager


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    create_timestamp = models.DateTimeField()
    timestamp = models.DateTimeField()
    language = models.CharField(max_length=56)
    wiki = models.CharField(max_length=256)
    category = ArrayField(models.CharField(max_length=256))
    title = models.CharField(max_length=256)
    auxiliary_text = ArrayField(models.CharField(max_length=256))

    objects = ContentManager()


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=256)

    objects = CategoryManager()


class CategoryContent(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    objects = CategoryContentManager()
