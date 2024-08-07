# Generated by Django 5.0.4 on 2024-04-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user_company',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, unique=True, verbose_name='Email'),
        ),
    ]
