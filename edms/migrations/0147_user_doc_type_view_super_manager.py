# Generated by Django 3.1.4 on 2021-05-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0146_auto_20210513_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_doc_type_view',
            name='super_manager',
            field=models.BooleanField(default=False),
        ),
    ]
