# Generated by Django 3.1.13 on 2022-10-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0035_auto_20221021_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_doc',
            name='company',
            field=models.CharField(default='ТДВ', max_length=3),
        ),
        migrations.AddField(
            model_name='order_doc',
            name='preamble',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
