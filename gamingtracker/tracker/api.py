from tracker.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

# User Viewset - CRUD api without having to specify explicit methods
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer