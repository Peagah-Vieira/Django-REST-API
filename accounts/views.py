from django.contrib.auth import get_user_model
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import AccountSerializer


class AccountAPIViewSet(ReadOnlyModelViewSet):
    serializer_class = AccountSerializer

    def get_queryset(self):
        User = get_user_model()
        queryset = User.objects.filter(username=self.request.user.username)
        return queryset