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
        User, on_delete=models.CASCADE, verbose_name='автор'
    )
    tags = models.ManyToManyField(Tag, through='TagToRecipe')
    ingredients = models.ManyToManyField(
        Ingredient, through='IngridientToRecipe'
    )

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

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


class IngridientToRecipe(models.Model):
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
