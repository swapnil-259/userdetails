# Generated by Django 2.0 on 2023-07-13 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20230713_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Taskno',
            new_name='Entryno',
        ),
    ]
