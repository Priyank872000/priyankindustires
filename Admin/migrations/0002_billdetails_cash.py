# Generated by Django 4.0.3 on 2022-07-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billdetails',
            name='cash',
            field=models.FloatField(default=0.0),
        ),
    ]
