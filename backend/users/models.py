from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    first_name = models.CharField('Имя', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150)
    email = models.EmailField('Почта', unique=True, max_length=150)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.username}: {self.email}'


class Follow(models.Model):
    """Модель подписки."""
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='Подписчик',
        default=User)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='Автор',
        default=User)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "username",
                    "author",
                ),
                name="unique_follow",
            ),
        )

    def __str__(self):
        return f'{self.username} follows {self.author}'
