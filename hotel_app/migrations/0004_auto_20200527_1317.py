# Generated by Django 3.0.5 on 2020-05-27 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_reservations_check_out_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservations',
            new_name='Reservation',
        ),
    ]
