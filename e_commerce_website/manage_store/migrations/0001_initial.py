# Generated by Django 4.1 on 2022-08-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_description', models.CharField(max_length=1000)),
                ('c_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
