from django.db import models
from django.db.models import Manager


class MyModel(models.Model):
    name = models.CharField(max_length=100)

    objects = Manager()
