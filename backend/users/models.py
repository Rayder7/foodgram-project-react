from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователи."""
    GUEST = 'guest'
    USER = 'user'
    ADMIN = 'admin'
    ROLES = [
        (USER, 'Аутентифицированный пользователь'),
        (GUEST, 'Гость'),
        (ADMIN, 'Администратор'),
    ]

    username = models.CharField(
        max_length=150,
        unique=True,
    )
    first_name = models.CharField('Имя', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150)
    email = models.EmailField('Почта', unique=True, max_length=150)
    password = models.CharField('Пароль', max_length=50)
    role = models.CharField(
        'Роль',
        max_length=max(len(role) for role, _ in ROLES),
        choices=ROLES,
        default=GUEST
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_together'
            )
        ]


class Follow(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False,
        blank=False, related_name='Подписчик',
        default=User)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False,
        blank=False, related_name='Автор',
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
