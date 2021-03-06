# Generated by Django 3.2 on 2021-04-29 05:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=200)),
                ('birth', models.DateField()),
                ('school', models.CharField(max_length=50)),
                ('grade', models.PositiveIntegerField(default=6, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('phone', models.CharField(max_length=20)),
                ('level', models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('create_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
