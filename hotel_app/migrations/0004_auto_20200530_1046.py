# Generated by Django 3.0.6 on 2020-05-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_feedback_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]