# Generated by Django 3.2.3 on 2021-05-30 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_playground', '0002_pizza_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('societies', models.ManyToManyField(through='relationship_playground.Membership', to='relationship_playground.Society')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship_playground.person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='society_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship_playground.society'),
        ),
    ]
