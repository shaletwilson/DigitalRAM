# Generated by Django 3.2.20 on 2023-08-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flight_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icao_code', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(blank=True, max_length=250, null=True)),
                ('type_model', models.CharField(blank=True, max_length=250, null=True)),
                ('wake', models.CharField(blank=True, max_length=50, null=True)),
                ('crew_min', models.CharField(blank=True, max_length=50, null=True)),
                ('PAX_min', models.CharField(blank=True, max_length=50, null=True)),
                ('PAX_max', models.CharField(blank=True, max_length=50, null=True)),
                ('propulsion', models.CharField(blank=True, max_length=250, null=True)),
                ('engine_model', models.CharField(blank=True, max_length=250, null=True)),
                ('engine_power', models.CharField(blank=True, max_length=250, null=True)),
                ('speed', models.CharField(blank=True, max_length=250, null=True)),
                ('service_ceiling', models.CharField(blank=True, max_length=250, null=True)),
                ('range', models.FloatField(blank=True, null=True)),
                ('empty_weight', models.FloatField(blank=True, null=True)),
                ('Max_takeoff_weight', models.FloatField(blank=True, null=True)),
                ('wing_span', models.FloatField(blank=True, null=True)),
                ('wing_area', models.FloatField(blank=True, null=True)),
                ('length', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('first_flight', models.CharField(blank=True, max_length=250, null=True)),
                ('production_status', models.CharField(blank=True, max_length=250, null=True)),
                ('total_production', models.CharField(blank=True, max_length=250, null=True)),
                ('data_for_version', models.CharField(blank=True, max_length=250, null=True)),
                ('variants', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
