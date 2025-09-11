from rest_framework.permissions import BasePermission

# Write your permissions here


class AuthPermission(BasePermission):
    def has_permission(self, request, view):
        authentication = getattr(view, "authentication", True)
        method = (getattr(request, "method")).lower()

        if not (
            authentication
            if isinstance(authentication, bool)
            else authentication.get(method)
        ):
            return True
        return request.user.is_authenticated
