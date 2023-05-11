from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    IngredientViewSet, TagViewSet, RecipeViewSet
)

app_name = 'recipes'

router_v1 = DefaultRouter()
router_v1.register('tags', TagViewSet, basename='tags')
router_v1.register('ingredients', IngredientViewSet, basename='ingredients')
router_v1.register('recipe', RecipeViewSet, basename='recipe')

urlpatterns = [
    path('', include(router_v1.urls)),
]
