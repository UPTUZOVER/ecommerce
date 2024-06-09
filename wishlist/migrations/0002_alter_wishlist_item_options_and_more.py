# Generated by Django 5.0.6 on 2024-05-19 16:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0010_rename_discount_product_chegirma"),
        ("wishlist", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="wishlist_item",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Wishlist Item",
                "verbose_name_plural": "Wishlist Items",
            },
        ),
        migrations.AlterUniqueTogether(
            name="wishlist_item",
            unique_together={("wishlist", "product")},
        ),
    ]