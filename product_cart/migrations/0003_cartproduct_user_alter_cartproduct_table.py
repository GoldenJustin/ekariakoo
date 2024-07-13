# Generated by Django 4.1.5 on 2023-01-28 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_cart', '0002_cartproduct_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='cartproduct',
            table='cartproduct',
        ),
    ]
