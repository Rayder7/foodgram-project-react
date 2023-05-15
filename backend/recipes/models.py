from django.db import models
from users.models import User


class Tag(models.Model):
    """Теги рецептов."""
    name = models.CharField('Название', max_length=200, unique=True)
    color = models.CharField(
        'Цвет', max_length=7, default="#ffffff", unique=True
    )
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = ('тег')
        verbose_name_plural = ("Теги")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингридиентов."""
    name = models.CharField('Название', max_length=100)
    measurement_unit = models.CharField('Еденица измерения', max_length=30)

    class Meta:
        verbose_name = ('Ингридиент')
        verbose_name_plural = ("Ингридиенты")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецепта."""
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Описание')
    cooking_time = models.PositiveIntegerField('Время приготовления')
    image = models.ImageField('Изображение')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='автор',
        related_name='recipes'
    )
    tags = models.ManyToManyField(
        Tag, through='TagToRecipe',
        verbose_name=('Теги'), related_name='recipes'
    )

    ingredients = models.ManyToManyField(
        Ingredient, through='IngredientToRecipe'
    )

    class Meta:
        verbose_name = ('Рецепт')
        verbose_name_plural = ('Рецепты')

    def __str__(self):
        return self.name


class TagToRecipe(models.Model):
    """Доп. таблица для связи тегов и рецептов."""
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='тег')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='рецепт'
    )

    class Meta:
        verbose_name = ('тег')
        verbose_name_plural = ("Теги")

    def __str__(self):
        return f'{self.tag} + {self.recipe}'


class IngredientToRecipe(models.Model):
    """Доп. таблица для связи ингридиентов и рецептов."""
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name='ингридиент'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='рецепт'
    )

    class Meta:
        verbose_name = ('ингридиент')
        verbose_name_plural = ("ингридиенты")

    def __str__(self):
        return f'{self.ingredient} + {self.recipe}'


class FavoriteRecipe(models.Model):
    """Модель избранных рецептов."""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name=('Рецепт'),
        related_name='in_favorite',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=('Пользователь'),
        related_name='favorite',
    )

    class Meta:
        verbose_name = ('Избранное')
        verbose_name_plural = ('Избранные')

    def __str__(self):
        return f' рецепт {self.recipe} в избранном пользователя {self.user}'


class ShopList(models.Model):
    """Модель списка покупок."""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name=('Рецепт'),
        related_name='shop_recipe',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=('Пользователь'),
        related_name='shop_user',
    )

    class Meta:
        verbose_name = ('Список покупок')
        verbose_name_plural = ('Списки покупок')

    def __str__(self):
        return f' рецепт {self.recipe} в избранном пользователя {self.user}'
