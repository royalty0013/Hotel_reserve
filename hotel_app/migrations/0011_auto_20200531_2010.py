# Generated by Django 3.0.6 on 2020-05-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0010_auto_20200531_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='nationality',
            field=models.CharField(choices=[('Nigeria', 'Nigeria'), ('Italy', 'Italy'), ('USA', 'USA'), ('United Kingdom', 'United Kingdom'), ('Ghana', 'Ghana')], max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='state',
            field=models.CharField(choices=[('Abia', 'Abia'), ('Edo', 'Edo'), ('Kogi', 'Kogi'), ('RIvers', 'RIvers'), ('Kano', 'kano')], max_length=50),
        ),
    ]
