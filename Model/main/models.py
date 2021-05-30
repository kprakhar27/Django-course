from django.db import models
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
    validate_slug
)
from main.validators import validate_even_number
# Create your models here.

# every table in database is represented as a class
# every row in databse is represented by an object of this class


class Student(models.Model):
    GENDERS = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('u', 'Undisclosed')
    )

    # varchar(100)
    name = models.CharField(max_length=100)
    # integer
    roll_number = models.IntegerField(unique=True)
    # Text
    address = models.TextField(null=True)
    # varchar(15)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    # varchar(255)
    email = models.CharField(
        max_length=255,
        null=True,
        validators=[EmailValidator("Email is not valid")]
    )
    # varchar(1)
    gender = models.CharField(max_length=1, choices=GENDERS, null=True)

    age = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(150),
            MinValueValidator(10),
            validate_even_number
        ]
    )

    slug = models.CharField(max_length=100, validators=[
                            validate_slug], null=True)

    def __str__(self):
        return self.name
