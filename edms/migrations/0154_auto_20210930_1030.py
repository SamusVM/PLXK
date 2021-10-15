# Generated by Django 3.1.13 on 2021-09-30 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0153_document_type_module_doc_type_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc_type_phase',
            name='doc_type_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='doc_type_phases', to='edms.document_type_version'),
        ),
    ]
