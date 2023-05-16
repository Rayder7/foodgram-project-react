from rest_framework import serializers

from .models import FavoriteRecipe, Ingredient, Recipe, ShopList, Tag


class TagSerializer(serializers.ModelSerializer):
    """Серилизатор для модели Tag."""
    class Meta:
        fields = ('name', 'color', 'slug')
        model = Tag


class IngredientSerializer(serializers.ModelSerializer):
    """Серилизатор для модели Ingredient."""
    class Meta:
        fields = ('name', 'measurement_unit')
        model = Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    """Серилизатор для модели Recipe."""
    class Meta:
        fields = (
            'name', 'text', 'cooking_time',
            'image', 'author', 'tags', 'ingredients'
        )
        model = Recipe


class FavoriteRecipeSerializer(serializers.ModelSerializer):
    """Серилизатор для модели FavoriteRecipe."""
    class Meta:
        fields = (
            'recipe', 'user'
        )
        model = FavoriteRecipe


class ShopListSerializer(serializers.ModelSerializer):
    """Серилизатор для модели Shoplist."""
    class Meta:
        fields = (
            'recipe', 'user'
        )
        model = ShopList
