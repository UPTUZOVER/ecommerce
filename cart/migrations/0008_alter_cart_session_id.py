# Generated by Django 5.0.6 on 2024-05-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='session_id',
            field=models.CharField(blank=True, default=' ', max_length=3000, null=True),
        ),
    ]