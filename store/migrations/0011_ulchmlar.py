# Generated by Django 5.0.6 on 2024-06-08 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0010_rename_discount_product_chegirma"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ulchmlar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ulcham_turlari",
                    models.CharField(
                        choices=[("color ", "color"), ("size", "size")], max_length=20
                    ),
                ),
                ("ulcham_qiymat", models.CharField(max_length=40)),
                ("is_active", models.BooleanField(default=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
            ],
        ),
    ]
