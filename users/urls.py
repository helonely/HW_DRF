from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListAPIView, PaymentCreateAPIView, PaymentRetrieveAPIView, \
    PaymentDestroyAPIView, PaymentUpdateAPIView

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payment/create", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("payments/<int:pk>/retrieve", PaymentRetrieveAPIView.as_view(), name="payment_detail"),
    path("payments/<int:pk>/delete", PaymentDestroyAPIView.as_view(), name="payment_delete"),
    path("payments/<int:pk>/update", PaymentUpdateAPIView.as_view(), name="payment_update"),
              ] + router.urls
