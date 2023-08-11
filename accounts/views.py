from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import AccountsSerializer


class WhoAmI(ReadOnlyModelViewSet):
    serializer_class = AccountsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        User = get_user_model()
        queryset = User.objects.filter(username=self.request.user.username)
        return queryset
    
    def list(self, request, *args, **kwargs):
        obj = self.get_queryset().first()
        serializer = self.get_serializer(instance=obj)
        return Response(serializer.data)

class ListUsers(ReadOnlyModelViewSet):
    serializer_class = AccountsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        User = get_user_model()
        queryset = User.objects.all()
        return queryset
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)