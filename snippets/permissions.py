from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_persmission(self, request, view, obj):
        if request.method in persmission.SAFE_METHODS:
            return True
        
        return obj.owner == request.user
