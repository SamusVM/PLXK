# Generated by Django 3.1.13 on 2021-10-04 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0156_auto_20211001_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_type_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='documents', to='edms.document_type_version'),
        ),
    ]
