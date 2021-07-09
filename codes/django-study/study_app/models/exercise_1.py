from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, blank=True)
    author_detail = models.OneToOneField("AuthorDetail", on_delete=models.PROTECT, blank=True, null=True)

    books = models.ManyToManyField(to="Book")

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.city


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    publish_day = models.DateField(blank=True, null=True)

    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
