# Generated by Django 4.1.7 on 2023-11-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_store', '0012_rename_user_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
