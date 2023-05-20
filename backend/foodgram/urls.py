from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

api_patt = [
    path('', include('users.urls', namespace='api_users')),
    path('', include('recipes.urls', namespace='api_recipes')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patt)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
