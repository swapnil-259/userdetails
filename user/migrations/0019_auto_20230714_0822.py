# Generated by Django 2.0 on 2023-07-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20230713_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='taskno',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
