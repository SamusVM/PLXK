# Generated by Django 3.1.13 on 2023-04-27 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0014_permission_permission_responsible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Bag_Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='boards/counterparties/client_bag_schemes/%Y/%m')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='bag_schemes', to='boards.counterparty')),
            ],
        ),
    ]
