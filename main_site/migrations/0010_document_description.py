# Generated by Django 3.2.3 on 2021-06-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0009_alter_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]
