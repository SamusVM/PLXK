# Generated by Django 3.1.13 on 2022-06-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0006_cost_rates_nom_cost_rates_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost_rates_product',
            name='department',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
