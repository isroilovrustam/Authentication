from rest_framework import generics, response, status
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import User
from django.contrib.auth import authenticate


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        password = self.request.data.get('password')
        username = self.request.data.get('username')
        if not User.objects.filter(username=username).first():
            return response.Response({'message': "User mavjud!"})
        user = authenticate(username=username, password=password)
        if user is None:
            return response.Response({'message': "Parol notog'ri!"})
        serializer = UserSerializer(user).data
        return response.Response(serializer, status=status.HTTP_200_OK)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
