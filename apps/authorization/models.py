from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Пользователю необходимо ввести свой e-mail')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create(
            email,
            password=password,
            **extra_fields
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    telegram_id = models.CharField(max_length=25,unique=True)


    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = []

    REQUIRED_FIELDS = ['email']


    objects = UserManager()

    def __str__(self):
        return f'Пользователь - {self.email}'
