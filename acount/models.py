from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re




class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None, user_company=None):

        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a username')

        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_company=user_company,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            user_company='company',
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def validate_url(value):
    # URL validation function
    # It should start with HTTP or HTTPS
    # The domain name can be a valid domain, IP address, or localhost
    # The port number and URL path are optional

    regex = re.compile(
        r'^(http|https)://'  # Protocol (http/https)
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Domain name
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6
        r'(?::\d+)?'  # Port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # URL path

    if not regex.match(value):
        raise ValidationError('Invalid URL format')

class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Ismingiz',
    )
    last_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Familiyangiz',
    )
    username = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Foydalanuvchi nomi',
        unique=True,
    )
    email = models.EmailField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Email',
        unique=True,
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?998\d{9}$',
                message='To\'g\'ri telefon raqamini kiriting.',
            ),
        ],
        blank=True,
        null=True,
        verbose_name='Telefon raqam',
    )
    user_company = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        unique=True,
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True





















































































































