# Generated by Django 3.2.3 on 2021-06-13 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_alter_review_mark'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='response',
            unique_together={('resume', 'vacancy')},
        ),
    ]
