# Generated by Django 5.0.6 on 2024-05-11 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_category_slug'),
        ('store', '0006_delete_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
