from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import *
from .models import User
from rest_framework.response import Response


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return UserReadSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.create_user(
            username=data.pop('username'),
            email=data.pop('email'),
            password=data.pop('password'),
            **data
        )
        return Response(UserReadSerializer(user), status=status.HTTP_201_CREATED)
