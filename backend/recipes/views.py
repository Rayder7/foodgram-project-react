from rest_framework import viewsets

from .models import Ingredient, Recipe, Tag
from .serializers import (IngredientSerializer, RecipeSerializer,
                          TagSerializer)


class IngredientViewSet(viewsets.ModelViewSet):
    """Вьюсет для IngredientSerializer."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ModelViewSet):
    """Вьюсет для TagSerializer."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """Вьюсет для RecipeSerializer."""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
