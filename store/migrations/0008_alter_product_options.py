# Generated by Django 5.0.6 on 2024-05-11 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]