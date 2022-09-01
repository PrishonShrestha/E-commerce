# Generated by Django 4.1 on 2022-09-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_updated_order_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='o_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=100),
        ),
    ]
