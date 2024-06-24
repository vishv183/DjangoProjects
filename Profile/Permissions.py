from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrSuperuser(permissions.BasePermission):
    """
    Custom permission to only allow owners or superusers to edit their profile.
    """

    def has_object_permission(self, request, view, obj):
        # Allow superuser to edit any user's profile.
        if request.user.is_superuser:
            return True

        # Allow users to edit their own profile.
        return obj == request.use


class DefaultPermission(BasePermission):
    def has_permission(self, request, view):
        # Your permission logic here
        return request.user and request.user.is_authenticated
