# Generated by Django 5.0.4 on 2024-04-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_description_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, help_text='Slug for the category', null=True, unique=True),
        ),
    ]
