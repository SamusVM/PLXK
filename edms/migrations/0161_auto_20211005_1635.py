# Generated by Django 3.1.13 on 2021-10-05 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0160_foyer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foyer',
            old_name='userprofile',
            new_name='employee',
        ),
    ]
