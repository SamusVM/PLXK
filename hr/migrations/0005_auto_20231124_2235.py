# Generated by Django 3.1.14 on 2023-11-24 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0163_doc_type_phase_plus_approval_by_chief'),
        ('accounts', '0042_userprofile_permissions_edit'),
        ('hr', '0004_auto_20231124_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='instructions', to='accounts.department'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='instructions', to='edms.seat'),
        ),
    ]
