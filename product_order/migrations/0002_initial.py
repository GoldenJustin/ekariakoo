# Generated by Django 4.1.7 on 2024-07-06 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_order', '0001_initial'),
        ('product_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_store.product'),
        ),
    ]
