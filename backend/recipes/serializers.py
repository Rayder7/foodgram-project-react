from rest_framework import serializers

from .models import Ingredient, Recipe, Tag


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
