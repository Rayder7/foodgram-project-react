from django.urls import include, path

app_name = 'recipes'

urlpatterns = [
    path('tags/', signup, name='tags'),
    path('recipes/', token, name='recipes'),
    path('ingredients/', token, name='ingredients'),
]
