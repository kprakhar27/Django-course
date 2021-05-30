from django.db import models
from django.core.validators import (
    MinValueValidator,
)

# Create your models here.

# Many - to - One Relationship


class Article(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)

    def __str__(self):
        return self.name

# Many - to - Many relationship


class Toppings(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField(validators=[
        MinValueValidator(0)
    ])
    toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=256)
    societies = models.ManyToManyField('Society', through='Membership')

    def __str__(self):
        return self.name


class Society(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Membership(models.Model):
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    society_id = models.ForeignKey('Society', on_delete=models.CASCADE)

    designation = models.CharField(max_length=256)
