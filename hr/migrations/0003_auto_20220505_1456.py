# Generated by Django 3.1.13 on 2022-05-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20220505_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department_regulation',
            name='staff_units',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='seat_instruction',
            name='staff_units',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
