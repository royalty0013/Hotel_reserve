# Generated by Django 3.0.6 on 2020-05-30 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0004_auto_20200530_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='added',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='added',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='updated',
        ),
    ]
