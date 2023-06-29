# Generated by Django 4.2.2 on 2023-06-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('detailing_type', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('weather_data', models.JSONField()),
            ],
        ),
    ]
