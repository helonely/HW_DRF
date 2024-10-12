from django.conf import settings
from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )

    description = models.TextField(
        verbose_name="Описание курса", help_text="Введите описание курса"
    )

    image = models.ImageField(
        verbose_name="Картинка курса",
        help_text="Загрузите картинку курса",
        upload_to="materials/images",
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="владелец",
        null=True,
        blank=True,
        help_text="Выберите владельца курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )

    description = models.TextField(
        verbose_name="Описание урока", help_text="Введите описание урока"
    )

    image = models.ImageField(
        verbose_name="Картинка урока",
        help_text="Загрузите картинку урока",
        upload_to="materials/images",
        null=True,
        blank=True,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Курс",
        help_text="Выберите курс",
    )

    video_url = models.URLField(
        verbose_name="ссылка на урок",
        null=True,
        blank=True,
        help_text="Введите ссылку на урок",
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="владелец",
        null=True,
        blank=True,
        help_text="Выберите владельца урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.name}"
