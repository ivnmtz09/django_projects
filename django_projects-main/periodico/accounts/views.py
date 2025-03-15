from rest_framework import generics, permissions
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from .models import Noticia
from .serializers import NoticiaSerializer

# Vista para autenticación básica
class LoginView(APIView):    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({"message": "Login exitoso"}, status=200)
        return Response({"error": "Credenciales inválidas"}, status=401)

class NoticiaListCreateView(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class NoticiaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer