# Generated by Django 5.0 on 2023-12-14 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]