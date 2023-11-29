from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if (
            request.user.is_superuser
            or request.user.is_staff
            or request.user.is_manager
        ):
            return True
        return obj.user == request.user
