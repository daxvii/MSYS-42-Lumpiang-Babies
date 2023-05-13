# Generated by Django 4.1.5 on 2023-04-25 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lumpiasys', '0008_alter_product_group_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='components',
            name='units_of_measurement',
        ),
        migrations.AddField(
            model_name='components',
            name='combo_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lumpiasys.combo'),
        ),
        migrations.AddField(
            model_name='components',
            name='item_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lumpiasys.product'),
        ),
    ]
