# Generated by Django 4.1.2 on 2022-11-02 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_rental_system', '0011_auto_20201024_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='status_end_date',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='status_start_date',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_status',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_class',
            field=models.CharField(choices=[('economy', 'Economy'), ('standard', 'Standard'), ('sport', 'Sport'), ('luxury', 'Luxury')], default='standard', max_length=9),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('car', 'Car'), ('truck', 'Truck'), ('van', 'Van'), ('suv', 'SUV')], default='car', max_length=8),
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_start', models.DateTimeField(blank=True, null=True)),
                ('status_end', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_system.vehicle')),
            ],
        ),
    ]