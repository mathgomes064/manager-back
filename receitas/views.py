from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from receitas.serializers import ReceitaSerializer
from rest_framework import generics
from .models import Receita
import ipdb

class ReceitaView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ReceitaSerializer
    queryset = Receita.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReceitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ReceitaSerializer
    queryset = Receita.objects.all()
    lookup_url_kwarg = "receita_id"
