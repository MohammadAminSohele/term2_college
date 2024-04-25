from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAdminUserOrUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and request.user.is_staff or
            request.user.is_authenticated and obj.user == request.user 
        )


class IsSuperuserOrStudentUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.student.user == request.user 
        )


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_superuser
        )
