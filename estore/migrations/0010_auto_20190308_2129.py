# Generated by Django 2.1.7 on 2019-03-08 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0009_auto_20190308_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='庫存數量'),
        ),
    ]
