from django.utils import timezone
from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Subscription
from users.models import User
from django.contrib.auth import get_user_model


@shared_task
def send_mail_update(course_id):
    """Отправка сообщения об обновлении курса по подписке"""
    subscription_course = Subscription.objects.filter(course=course_id)
    print(f"Найдено {len(subscription_course)} подписок на курс {course_id}")
    for subscription in subscription_course:
        print(f"Отправка электронного письма на {subscription.user.email}")
        send_mail(
            subject="Обновление материалов курса",
            message=f'Курс {subscription.course.name} был обновлен.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=False
        )


@shared_task
def check_inactive_users():
    """Проверка последнего входа пользователей и отключение неактивных пользователей"""
    user = get_user_model()
    inactive_users = user.objects.filter(
        last_login__lte=timezone.now() - timedelta(days=30), is_active=True
    )
    for user in inactive_users:
        user.is_active = False
        user.save()
