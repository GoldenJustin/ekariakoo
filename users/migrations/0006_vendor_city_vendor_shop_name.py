# Generated by Django 4.1.7 on 2023-11-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='vendor',
            name='shop_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
