# Generated by Django 5.0 on 2023-12-14 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_contact_umber_usercreateform_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercreateform',
            name='contact_number',
        ),
    ]