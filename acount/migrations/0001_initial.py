# Generated by Django 5.0.4 on 2024-04-22 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ismingiz')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Familiyangiz')),
                ('username', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Foydalanuvchi nomi')),
                ('email', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="To'g'ri telefon raqamini kiriting.", regex='^\\+?998\\d{9}$')], verbose_name='Telefon raqam')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
