# Generated by Django 5.0 on 2023-12-14 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_confirmpassword_usercreateform_confirm_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercreateform',
            old_name='contact_umber',
            new_name='contact_number',
        ),
    ]