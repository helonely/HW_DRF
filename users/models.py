from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


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


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    payment_date = models.DateField(verbose_name="Дата оплаты", auto_now_add=True)

    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="оплаченный курс",
        null=True,
        blank=True,
    )

    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="оплаченный урок",
        null=True,
        blank=True,
    )

    payment_amount = models.PositiveIntegerField(
        verbose_name="Сумма оплаты",
        help_text="Введите сумму оплаты",
    )

    payment_method = models.CharField(
        max_length=50,
        choices=[
            ("cash", "Наличными"),
            ("bank_transfer", "Перевод на счет"),
        ],
        default="bank_transfer",
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
    )

    session_id = models.CharField(
        max_length=255,
        verbose_name='ID сессии',
        blank=True,
        null=True,
    )

    link = models.URLField(
        max_length=400,
        verbose_name='Ссылка на оплату',
        blank=True,
        null=True,
        help_text='Перейдите по этой ссылке, чтобы оплатить продукт'
    )

    def __str__(self):
        if self.paid_course:
            return f"Дата платежа {self.payment_date}, за курс {self.paid_course} на сумму {self.payment_amount:.2f} руб."
        return f"Дата платежа {self.payment_date} за урок {self.paid_lesson} на сумму {self.payment_amount:.2f} руб."

    class Meta:
        ordering = ["-payment_date"]
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
