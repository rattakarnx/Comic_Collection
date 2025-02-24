# Generated by Django 2.2.17 on 2020-11-14 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201112_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='comicinput',
            name='Series',
            field=models.CharField(choices=[('First', '1st'), ('Second', '2nd'), ('Third', '3rd')], default='1st', max_length=30),
        ),
        migrations.AddField(
            model_name='comicinput',
            name='Type',
            field=models.CharField(choices=[('Regular', 'Reg'), ('Annual', 'Ann'), ('Special', 'Spc')], default='Reg', max_length=30),
        ),
        migrations.AlterField(
            model_name='comicinput',
            name='Grade',
            field=models.CharField(choices=[('Mint', 'MT'), ('NMPLUS', 'NM+'), ('NM', 'NM'), ('NMM', 'NM-'), ('NM/VF', 'NM/VF'), ('VF', 'VF'), ('F', 'F'), ('VG', 'VG'), ('G', 'G')], default='NM/VF', max_length=30),
        ),
        migrations.AlterField(
            model_name='comicinput',
            name='SellingNotes',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
