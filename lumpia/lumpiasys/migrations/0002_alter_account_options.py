# Generated by Django 4.1.5 on 2023-05-13 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumpiasys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': (('owner', 'can view remaining inventory'), ('staff', 'cannot view remaining inventory'))},
        ),
    ]
