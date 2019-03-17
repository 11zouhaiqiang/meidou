from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
