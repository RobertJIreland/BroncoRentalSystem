# Generated by Django 2.2.1 on 2019-10-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/vehicle_pics'),
        ),
    ]
