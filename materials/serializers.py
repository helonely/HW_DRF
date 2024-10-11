from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField()

    def get_lessons(self, course):
        return [lesson.description for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseCountSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    course = CourseSerializer()

    def get_count_lesson(self, lesson):
        return Lesson.objects.filter(course=lesson).count()

    class Meta:
        model = Lesson
        fields = ("name", "description", "count_lesson", "image", "video_url", "course")
