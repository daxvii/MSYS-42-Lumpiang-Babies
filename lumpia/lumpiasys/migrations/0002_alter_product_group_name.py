# Generated by Django 4.1.5 on 2023-01-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumpiasys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
