# Generated by Django 4.1 on 2022-08-31 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_added_order_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='op_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='op_quantity',
            new_name='quantity',
        ),
    ]
