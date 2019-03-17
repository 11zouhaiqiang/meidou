# Create your views here.
from rest_framework.generics import CreateAPIView
from users.serializer import CreateUserSerializer


class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializer
