# Generated by Django 5.0.4 on 2024-05-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('bio', models.TextField()),
                ('phone_no', models.CharField(max_length=12)),
            ],
        ),
    ]
