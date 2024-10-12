from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", viewset=CourseViewSet, basename="materials")


urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path(
        "lessons/<int:pk>/retrieve",
        LessonRetrieveAPIView.as_view(),
        name="lesson-retrieve",
    ),
    path("lessons/create", LessonCreateAPIView.as_view(), name="lesson_create"),
    path(
        "lessons/<int:pk>/update", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path(
        "lessons/<int:pk>/delete", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
] + router.urls
