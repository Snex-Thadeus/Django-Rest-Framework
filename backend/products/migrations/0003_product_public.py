# Generated by Django 4.1.1 on 2022-09-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]