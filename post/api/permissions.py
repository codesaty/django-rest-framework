from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You must be the owener of this object."

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) or request.user.is_superuser
