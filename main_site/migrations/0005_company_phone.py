# Generated by Django 3.2.3 on 2021-06-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_auto_20210610_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(default=' ', max_length=12, verbose_name='Телефон'),
        ),
    ]