# Generated by Django 4.0.5 on 2022-07-08 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipl_data_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeliveriesDataModel',
        ),
        migrations.DeleteModel(
            name='MatchesDataModel',
        ),
    ]
