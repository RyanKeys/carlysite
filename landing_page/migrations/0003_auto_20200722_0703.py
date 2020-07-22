# Generated by Django 2.2.6 on 2020-07-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_auto_20200722_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='url',
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]