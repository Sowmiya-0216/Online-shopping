# Generated by Django 5.1.7 on 2025-03-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
            ],
        ),
    ]
