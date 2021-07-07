from django.db import models


class MyModel(models.Model):
    boolean_field = models.BooleanField(default=False)
    char_field = models.CharField(max_length=50, null=True)
    integer_field = models.IntegerField(null=True)
    date_field = models.DateField(null=True)
    datetime_field = models.DateTimeField(null=True)

    objects = models.Manager()
