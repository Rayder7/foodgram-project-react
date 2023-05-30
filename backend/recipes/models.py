from colorfield.fields import ColorField
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from users.models import User


class Tag(models.Model):
    """Теги рецептов."""
    name = models.CharField('Название', max_length=200, unique=True)
    color = ColorField(
        'Цвет', max_length=7, default="#ffffff", unique=True, format='hex',
        validators=[
            RegexValidator(
                regex="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                message='Проверьте вводимый формат',
            )
        ],
    )
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингридиентов."""
    name = models.CharField('Название', max_length=100, db_index=True)
    measurement_unit = models.CharField('Еденица измерения', max_length=30)

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='unique_name_measurement_unit'
            )
        ]

    def __str__(self):
        return f'{self.name[:10]} {self.measurement_unit}'


class Recipe(models.Model):
    """Модель рецепта."""
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Описание')
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[
            MinValueValidator(
                1, message='Минимальное время готовки не менее 1 минуты'),
            MaxValueValidator(600)
        ]
    )
    image = models.ImageField('Изображение', upload_to='recipes/image/')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='автор',
        related_name='recipes'
    )
    tags = models.ManyToManyField(
        Tag, through='TagToRecipe',
        verbose_name=('Теги'),
        related_name='recipes'
    )

    ingredients = models.ManyToManyField(
        Ingredient, through='IngredientToRecipe',
        verbose_name='Ингридиенты',
        related_name='recipes'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = ('Рецепт')
        verbose_name_plural = ('Рецепты')

    def __str__(self):
        return self.name[:10]


class TagToRecipe(models.Model):
    """Доп. таблица для связи тегов и рецептов."""
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='тег',
                            related_name="tag_recipe")
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='рецепт',
        related_name="recipe_tag"
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.tag} + {self.recipe[:10]}'


class Favorite(models.Model):
    """ Модель добавление в избраное. """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name="in_favorite"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name="favorite"
    )

    class Meta:
        auto_created = True
        verbose_name = 'Избранные рецепты'

        def __str__(self):
            return (f' рецепт {Favorite.recipe}'
                    f'в избранном пользователя {Favorite.user}')


class ShopList(models.Model):
    """Модель списка покупок."""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name="shop_recipe"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name="shop_user"
    )

    class Meta:
        auto_created = True
        verbose_name = 'Корзина покупок'

    def __str__(self):
        return (f' рецепт {ShopList.recipe}'
                f'в корзине пользователя {ShopList.user}')


class IngredientToRecipe(models.Model):
    """Доп. таблица для связи ингридиентов и рецептов."""
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name='ингридиент',
        related_name="ingredient_recipe",
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='рецепт',
        related_name='recipe_ingredient'

    )

    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2600)],
        verbose_name='Количество ингредиента',
        default=1
    )

    class Meta:
        verbose_name = 'ингридиент'
        verbose_name_plural = 'ингридиенты'

    def __str__(self):
        return f'{self.ingredient[:10]} + {self.recipe[:10]}'
