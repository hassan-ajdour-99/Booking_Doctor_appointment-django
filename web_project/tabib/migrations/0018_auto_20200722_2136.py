# Generated by Django 3.0.5 on 2020-07-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabib', '0017_auto_20200722_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='field',
            field=models.CharField(blank=True, choices=[('a', 'Dentist'), ('a', 'psychologist'), ('a', 'eyes Doctor'), ('a', 'Physiologist')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='whatssap',
            field=models.CharField(blank=True, default='+2126', max_length=13, null=True),
        ),
    ]