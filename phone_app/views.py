from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import User
from .serializers import UserSerializer
from .filters import UserFilter


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

