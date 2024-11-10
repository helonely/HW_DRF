from django.contrib import admin

from materials.models import Course, Lesson, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "image",
        "owner",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "image",
        "course",
        "video_url",
        "owner",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "course",
    )
