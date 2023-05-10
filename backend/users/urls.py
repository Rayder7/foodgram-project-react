from django.urls import include, path

app_name = 'users'

urlpatterns = [
    path('', signup, name='list'),
    path('subcriptions/', token, name='subcriptions'),
]
