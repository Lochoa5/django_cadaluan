# Generated by Django 5.0.1 on 2024-02-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nick',
            field=models.CharField(default='user', max_length=100, unique=True),
        ),
    ]
