from rest_framework import permissions


class IsAdminOnly(permissions.BasePermission):
    """Разрешения для админа."""
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.user.method in permissions.SAFE_METHODS
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return request.user.method in permissions.SAFE_METHODS
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin)


class IsUserOnly(permissions.BasePermission):
    """Разрешения для авторизованных юзеров."""
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and (
            request.user.is_admin or obj.author == request.user
                or request.method == 'POST'):
            return True
        return request.method in permissions.SAFE_METHODS
