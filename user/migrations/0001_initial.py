# Generated by Django 2.0 on 2023-07-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('Address', models.CharField(max_length=150)),
                ('Stay', models.CharField(choices=[('H', 'Hostel'), ('D', 'Day_Scholar')], max_length=1)),
                ('Password', models.CharField(default='', max_length=200)),
                ('Status', models.CharField(default='', max_length=2)),
            ],
        ),
    ]
