# Generated by Django 4.2.3 on 2023-08-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='доступен для редактирования'),
        ),
    ]