# Generated by Django 5.0.6 on 2024-05-13 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_chegirma_product_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount',
            new_name='chegirma',
        ),
    ]
