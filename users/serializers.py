from rest_framework import serializers

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "payment_date", "payment_amount", "payment_method", "session_id", "link", "user"]


class UserSerializer(serializers.ModelSerializer):
    payment_history = PaymentSerializer(source="payment_set", read_only=True, many=True)

    class Meta:
        model = User
        fields = "__all__"


class OtherUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "phone",
            "city",
            "avatar",
        )
