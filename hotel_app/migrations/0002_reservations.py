# Generated by Django 3.0.5 on 2020-05-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_date', models.DateField()),
                ('guest_no', models.PositiveIntegerField()),
                ('room_type', models.CharField(max_length=100)),
            ],
        ),
    ]
