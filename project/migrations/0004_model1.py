# Generated by Django 5.1.7 on 2025-03-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_delete_model1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
