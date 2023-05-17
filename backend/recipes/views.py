from rest_framework import viewsets
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .permissions import IsAdminOnly, IsUserOnly
from .models import Ingredient, Recipe, Tag
from .serializers import (IngredientSerializer,
                          RecipeSerializer,
                          TagSerializer)


class IngredientViewSet(viewsets.ModelViewSet):
    """Вьюсет для IngredientSerializer."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ModelViewSet):
    """Вьюсет для TagSerializer."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsUserOnly,)


class RecipeViewSet(viewsets.ModelViewSet):
    """Вьюсет для RecipeSerializer."""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsUserOnly,)

    def favorite_shopping_post_delete(self, obj):
        recipe = self.get_object()
        if self.request.method == 'DELETE':
            obj.get(recipe_id=recipe.id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if obj.filter(recipe=recipe).exists():
            raise ValidationError('Рецепт уже в избранном')
        obj.create(recipe=recipe)
        serializer = RecipeSerializer(instance=recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True,
            methods=['POST', 'DELETE'],
            permission_classes=(permissions.IsAuthenticated,))
    def favorite(self, request, pk=None):
        return self.favorite_shopping_post_delete(request.user.favorite)

    @action(methods='GET', detail=False, url_path='download_shopping_cart',
            url_name='download_shopping_cart')
    def download_shopping_cart(self, request):
        Ingredients = Ingredient.objects.all()
        return Ingredients

    @action(methods=['POST', 'DELETE'], detail=True,
            permission_classes=(permissions.IsAuthenticated,))
    def shopping_cart(self, request, pk=None):
        return request.user.shop_user
