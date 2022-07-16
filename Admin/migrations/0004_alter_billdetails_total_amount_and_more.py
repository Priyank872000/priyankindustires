# Generated by Django 4.0.3 on 2022-07-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_remove_billdetails_cash_payment_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetails',
            name='total_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='productselling',
            name='qty',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='productselling',
            name='rate',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
