# Generated by Django 4.0.4 on 2022-05-03 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_remove_cv_title_cv_address_cv_email_cv_name_cv_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='phone',
        ),
    ]