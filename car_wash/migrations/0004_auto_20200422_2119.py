# Generated by Django 3.0.3 on 2020-04-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0003_auto_20200422_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='discount_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='grant_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]