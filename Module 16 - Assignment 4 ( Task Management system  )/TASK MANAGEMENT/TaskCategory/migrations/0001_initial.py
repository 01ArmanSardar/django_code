# Generated by Django 5.0.6 on 2024-05-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoryname', models.CharField(max_length=20)),
                ('Tasks', models.ManyToManyField(to='Task.taskmodel')),
            ],
        ),
    ]
