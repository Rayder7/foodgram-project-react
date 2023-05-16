# Generated by Django 3.2 on 2023-05-15 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(default=users.models.User, on_delete=django.db.models.deletion.CASCADE, related_name='Автор', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(default=users.models.User, on_delete=django.db.models.deletion.CASCADE, related_name='Подписчик', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('username', 'author'), name='unique_follow'),
        ),
    ]