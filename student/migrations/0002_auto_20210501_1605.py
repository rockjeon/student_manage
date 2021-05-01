# Generated by Django 3.2 on 2021-05-01 07:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.CharField(choices=[('Library', 'Library'), ('Voca', 'Voca'), ('NF', 'Library')], max_length=30)),
                ('library', models.CharField(choices=[('R(1:20)', 'R(1:20)'), ('S(1:40)', 'S(1:40)'), ('I(2:00)', 'I(2:00)')], max_length=30)),
                ('voca_library', models.CharField(choices=[('RV(1:40)', 'RV(1:40)'), ('SV(2:00)', 'SV(2:00)'), ('IV(2:20)', 'I(2:20)')], max_length=30)),
                ('count', models.CharField(choices=[('12', '12'), ('24', '24'), ('36', '36'), ('48', '48')], max_length=30)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]