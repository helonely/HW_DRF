from rest_framework.exceptions import ValidationError

from materials.models import Subscription


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = value.get(self.field, [])
        if 'youtube.com' not in link:
            raise ValidationError('Оставьте ссылку на видео')


class SubscriptionValidator:
    def __call__(self, attrs):
        user = attrs.get('user')
        course = attrs.get('course')
        owner = attrs.get('owner')
        if user and course and owner and Subscription.objects.filter(user=user, course=course, owner=owner).exists():
            raise ValidationError('Подписка на данный курс уже активна')
