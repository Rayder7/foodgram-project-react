from django.contrib import admin

from .models import FavoriteRecipe, Ingredient, Recipe, ShopList, Tag


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'in_favorite')
    list_filter = ('name', 'author', 'tags')
    empty_value_display = '-пусто-'

    def in_favorite(self, obj):
        return obj.in_favorite.all().count()


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


class ShoplistAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(FavoriteRecipe, FavoriteRecipeAdmin)
admin.site.register(ShopList, ShoplistAdmin)
