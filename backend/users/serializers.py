from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer

from .models import Follow, User
from recipes.models import Recipe


class CustomUserSerializer(UserSerializer):
    """Серилизатор для модели User."""
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'password', 'role', 'is_subscribed'
        )
        model = User

    def get_is_sub(self, obj):
        """Проверка подписан ли юзер на автора."""
        request = self.context.get('request')
        if not request or request.user.is_anonymoues:
            return False
        return Follow.objects.filter(user=self.context['request'].user,
                                     author=obj).exists()


class CreateUserSeralizer(UserCreateSerializer):
    """Сериализатор для создания юзера."""
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'password'
        )


class FollowRecipeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для короткой модели рецепта в подписках.
    """
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для подписок.
    """
    is_subscribed = serializers.SerializerMethodField(read_only=True)
    recipes = serializers.SerializerMethodField(read_only=True)
    recipes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count',
        )

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if not user:
            return False
        return Follow.objects.filter(user=user, author=obj).exists()

    def get_recipes(self, obj):
        request = self.context.get('request')
        limit_recipes = request.query_params.get('recipes_limit')
        if limit_recipes is not None:
            recipes = obj.recipes.all()[:(int(limit_recipes))]
        else:
            recipes = obj.recipes.all()
        context = {'request': request}
        return FollowRecipeSerializer(recipes, many=True,
                                      context=context).data

    @staticmethod
    def get_recipes_count(obj):
        return obj.recipes.count()
