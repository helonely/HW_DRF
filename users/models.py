from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите вашу почту"
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон",
        help_text="Введите ваш телефон",
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Введите ваш город",
        blank=True,
        null=True,
    )

    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to="users/avatars",
        help_text="Загрузите ваш аватар",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"
