# Generated by Django 4.1 on 2022-08-31 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_store', '0010_Updated__Product_Model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_description',
            field=models.CharField(max_length=500),
        ),
    ]
