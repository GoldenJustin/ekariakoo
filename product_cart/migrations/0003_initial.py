# Generated by Django 4.1.7 on 2024-07-06 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('product_store', '0001_initial'),
        ('product_cart', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.account'),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='variation',
            field=models.ManyToManyField(blank=True, to='product_store.variation'),
        ),
    ]
