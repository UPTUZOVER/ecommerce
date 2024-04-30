# Generated by Django 5.0.4 on 2024-04-23 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='true_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Haqiqiy narx'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Maxsulot nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0, help_text='Mahsulot chegirma miqdorini kiriting.', validators=[django.core.validators.MinValueValidator(0, message="Satish mikdori 0 yoki undan katta bo'lishi kerak."), django.core.validators.MaxValueValidator(100, message="Sotish mikdori 100 yoki undan kam bo'lishi kerak.")], verbose_name='Sotish Mikdori'),
        ),
    ]