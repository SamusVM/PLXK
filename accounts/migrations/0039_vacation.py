# Generated by Django 3.1.13 on 2022-10-11 06:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_userprofile_corr_template_edit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(default=django.utils.timezone.now)),
                ('end', models.DateField(null=True)),
                ('started', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('acting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='acting_for', to='accounts.userprofile')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='vacations', to='accounts.userprofile')),
            ],
        ),
    ]
