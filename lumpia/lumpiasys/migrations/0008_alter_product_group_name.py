# Generated by Django 4.1.5 on 2023-04-19 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lumpiasys', '0007_rename_name_combo_combo_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lumpiasys.group'),
        ),
    ]