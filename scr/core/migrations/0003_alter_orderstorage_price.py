# Generated by Django 4.2 on 2023-05-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_name_callapplication_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstorage',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
