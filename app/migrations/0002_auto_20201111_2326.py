# Generated by Django 2.2.17 on 2020-11-11 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comicinput',
            options={'ordering': ('Title',)},
        ),
        migrations.RemoveField(
            model_name='comicinput',
            name='email_confirmed',
        ),
    ]
