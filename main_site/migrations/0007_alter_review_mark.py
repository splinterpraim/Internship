# Generated by Django 3.2.3 on 2021-06-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_auto_20210613_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.CharField(choices=[('excellent', 'Отлично'), ('good', 'Хорошо'), ('normal', 'Нормально'), ('bad', 'Плохо')], default='good', max_length=10, verbose_name='Оценка'),
        ),
    ]
