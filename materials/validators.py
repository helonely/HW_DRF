from rest_framework.exceptions import ValidationError


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = value.get(self.field, [])
        if 'youtube.com' not in link:
            raise ValidationError('Оставьте ссылку на видео')
