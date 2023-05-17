from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from djoser import utils
from djoser.views import TokenDestroyView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Follow, User
from .serializers import (FollowSerializer,)


def follow_author(request, pk):
    """Подписка на автора."""
    user = get_object_or_404(User, username=request.user.username)
    author = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        if user.id == author.id:
            content = {'errors': 'Подписаться на себя нельзя'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        try:
            Follow.objects.create(user=user, author=author)
        except Exception:
            content = {'errors': 'Подписка уже оформлена!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        follows = User.objects.all().filter(username=author)
        seialiser = FollowSerializer(
            follows,
            context={'request': request},
            many=True
        )
        return Response(seialiser.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        try:
            subscription = Follow.objects.get(user=user, author=author)
        except Exception:
            content = {'errors': 'Вы не подписаны на данного автора'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        subscription.delete()
        return HttpResponse('Вы успешно отписаны от этого автора',
                            status=status.HTTP_204_NO_CONTENT)


class SubscriptionListView(viewsets.ReadOnlyModelViewSet):
    """Вью для генерации списка подписок пользователя."""
    queryset = User.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def get_gyeryset(self):
        user = self.request.user
        new_queryset = User.objects.filter(fallowing__user=user)
        return new_queryset


class CustomTokenDestroyView(TokenDestroyView):

    def post(self, request):
        utils.logout_user(request)
        return Response(status=status.HTTP_201_CREATED)
