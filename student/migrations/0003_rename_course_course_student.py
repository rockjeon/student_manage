# Generated by Django 3.2 on 2021-05-01 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210501_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course',
            new_name='student',
        ),
    ]