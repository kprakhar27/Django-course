# Generated by Django 3.2.3 on 2021-05-30 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=255, null=True, validators=[django.core.validators.EmailValidator('Email is not valid')]),
        ),
    ]
