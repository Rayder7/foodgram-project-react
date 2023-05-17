from djoser.views import TokenCreateView
from rest_framework.routers import DefaultRouter
from .views import CustomTokenDestroyView, SubscriptionListView, follow_author
from django.urls import include, path

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register(
    r'users/subscriptions', SubscriptionListView, basename='sub'
    )

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include(router_v1.urls)),
    path('auth/token/login/',
         TokenCreateView.as_view(),
         name='login'),
    path('auth/token/logout/',
         CustomTokenDestroyView.as_view(),
         name='logout'),
    path('users/<int:pk>/subscribe/',
         follow_author,
         name='follow-author'),
]
