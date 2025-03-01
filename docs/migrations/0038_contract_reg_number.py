# Generated by Django 4.2.11 on 2025-02-10 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0037_auto_20231206_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract_Reg_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('date', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='reg_number', to='docs.contract')),
            ],
        ),
    ]
