# Generated by Django 2.0 on 2023-07-13 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20230713_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='data',
            new_name='Task',
        ),
    ]