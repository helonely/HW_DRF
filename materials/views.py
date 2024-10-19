from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED

from materials.models import Course, Lesson, Subscription
from materials.paginators import LearningPagination, LessonPagination
from materials.serializers import (CourseCountSerializer, CourseSerializer,
                                   LessonSerializer, SubscriptionSerializer)
from users.permissions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseCountSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve", "list"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action in ["create", "destroy"]:
            self.permission_classes = (IsOwner | ~IsModer,)
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if IsModer().has_permission(self.request, self):
                return Course.objects.all()
            return Course.objects.filter(owner=user)
        return Course.objects.none()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated, IsModer | IsOwner]
    pagination_class = LessonPagination
    search_fields = [
        "name",
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if IsModer().has_permission(self.request, self):
                return Lesson.objects.all()
            return Lesson.objects.filter(owner=user)
        return Lesson.objects.none()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if IsModer().has_permission(self.request, self):
                return Lesson.objects.all()
            return Lesson.objects.filter(owner=user)
        return Lesson.objects.none()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if IsModer().has_permission(self.request, self):
                return Lesson.objects.all()
            return Lesson.objects.filter(owner=user)
        return Lesson.objects.none()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | ~IsModer]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subscription_item = Subscription.objects.filter(user=user, course=course_item).first()

        if subscription_item:
            subscription_item.delete()
            message = 'подписка удалена'
            status = HTTP_204_NO_CONTENT
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
            status = HTTP_201_CREATED

        return Response({'message': message}, status=status)


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    pagination_class = LearningPagination
    permission_classes = [IsAuthenticated, IsOwner]
