# Generated by Django 3.1.13 on 2022-04-01 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0152_document_type_module_defines_doc_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc_registration',
            name='registration_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
