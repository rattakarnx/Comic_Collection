# Generated by Django 2.2.17 on 2021-01-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20210109_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicinput',
            name='year',
            field=models.IntegerField(blank=True, default='', null=True, verbose_name='year'),
        ),
    ]
