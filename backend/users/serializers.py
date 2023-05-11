from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Серилизатор для модели User."""
    class Meta:
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password', 'role'
        )
        model = User
