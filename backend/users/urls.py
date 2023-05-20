from djoser.views import TokenCreateView
from rest_framework.routers import DefaultRouter
from .views import CustomTokenDestroyView, SubscriptionListView, follow_author
from django.urls import include, path

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register(
    r'users/subscriptions', SubscriptionListView, basename='subscriptions'
    )

urlpatterns = [
    path('users/<int:pk>/subscribe/',
         follow_author,
         name='follow-author'),
    path(r'', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),

]
