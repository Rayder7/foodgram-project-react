from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import include, path

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]
