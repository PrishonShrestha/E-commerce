# Generated by Django 4.1 on 2022-08-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_store', '0002_alter_category_c_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='c_img',
            field=models.ImageField(upload_to=''),
        ),
    ]