# Generated by Django 3.2.3 on 2021-06-15 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0010_document_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='photo',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фото'),
        ),
    ]
