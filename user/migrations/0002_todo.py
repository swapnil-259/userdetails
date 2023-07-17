# Generated by Django 2.0 on 2023-07-13 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('Taskno', models.AutoField(primary_key=True, serialize=False)),
                ('Task', models.CharField(max_length=255)),
                ('Tasktime', models.DateTimeField(auto_now_add=True)),
                ('UpdateTask', models.BooleanField(default=False)),
                ('Updatetime', models.DateTimeField(auto_now_add=True)),
                ('DeleteTask', models.BooleanField(default=False)),
                ('Deletetime', models.DateTimeField(auto_now_add=True)),
                ('CompleteTask', models.BooleanField(default=False)),
                ('Completetime', models.DateTimeField(auto_now_add=True)),
                ('Identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Register_user')),
            ],
        ),
    ]