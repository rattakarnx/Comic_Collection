# Generated by Django 2.2.17 on 2020-11-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201115_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicinput',
            name='BackPic',
            field=models.ImageField(blank=True, default='Comic_Pics/default.png', upload_to='Comic_Pic/'),
        ),
        migrations.AlterField(
            model_name='comicinput',
            name='ContentPic',
            field=models.ImageField(blank=True, default='Comic_Pics/default.png', upload_to='Comic_Pics'),
        ),
        migrations.AlterField(
            model_name='comicinput',
            name='CoverPic',
            field=models.ImageField(blank=True, default='Comic_Pics/default.png', upload_to='Comic_Pics'),
        ),
    ]
