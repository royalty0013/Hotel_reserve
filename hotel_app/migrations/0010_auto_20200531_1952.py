# Generated by Django 3.0.6 on 2020-05-31 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0009_auto_20200531_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_adult',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=20),
        ),
    ]
