import json

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    """
    Добавляем ингредиенты из файла CSV.
    После миграции БД запускаем командой
    python manage.py load_ingredients локально
    или
    sudo docker-compose exec backend python manage.py load_ingredients
    на удаленном сервере.
    Создает записи в модели Ingredients из списка.
    """
    help = 'Load ingredients data from csv-file to DB.'

    def handle(self, *args, **kwargs):
        with open(
                'recipes/data/ingredients.json', 'r',
                encoding='UTF-8'
        ) as ingredients:
            ingredient_data = json.loads(ingredients.read())
            for ingredients in ingredient_data:
                Ingredient.objects.get_or_create(**ingredients)
        self.stdout.write(self.style.SUCCESS('Данные загружены'))
