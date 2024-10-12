from django.urls import path
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentCreateAPIView, PaymentDestroyAPIView,
                         PaymentListAPIView, PaymentRetrieveAPIView,
                         PaymentUpdateAPIView, UserViewSet)

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payment/create", PaymentCreateAPIView.as_view(), name="payment_create"),
    path(
        "payments/<int:pk>/retrieve",
        PaymentRetrieveAPIView.as_view(),
        name="payment_detail",
    ),
    path(
        "payments/<int:pk>/delete",
        PaymentDestroyAPIView.as_view(),
        name="payment_delete",
    ),
    path(
        "payments/<int:pk>/update",
        PaymentUpdateAPIView.as_view(),
        name="payment_update",
    ),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login/",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
] + router.urls
