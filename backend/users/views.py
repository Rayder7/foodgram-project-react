from rest_framework import viewsets

from .models import User
from .serializers import (UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для IngredientSerializer."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
