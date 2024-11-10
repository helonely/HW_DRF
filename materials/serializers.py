from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidator, SubscriptionValidator


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField(read_only=True)

    @staticmethod
    def get_lessons(course):
        return [lesson.description for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            LinkValidator(field='video_url'),
        ]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        validators = [
            SubscriptionValidator(),
        ]


class CourseCountSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    course = CourseSerializer()
    subscription = serializers.SerializerMethodField()

    @staticmethod
    def get_count_lesson(course):
        return Lesson.objects.filter(course=Lesson.course).count()

    def get_subscription(self, obj):
        if Subscription.objects.filter(course=obj, user=self.context.get('request', None).user.id):
            return True
        return False

    class Meta:
        model = Lesson
        fields = ("name", "description", "count_lesson", "image", "video_url", "course", "subscription")
