# Generated by Django 3.1.6 on 2021-06-10 03:48

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshopName', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(default=9999999999)),
                ('latitude', models.DecimalField(decimal_places=9, default=0, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=9, default=0, max_digits=12)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(default=' ', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.DecimalField(decimal_places=9, default=0, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=9, default=0, max_digits=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.workshopaccount')),
            ],
        ),
    ]
