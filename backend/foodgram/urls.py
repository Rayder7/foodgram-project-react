from django.contrib import admin
from django.urls import include, path


api_patt = [
    path('', include('users.urls', namespace='api_users')),
    path('', include('recipes.urls', namespace='api_recipes')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patt)),
]
