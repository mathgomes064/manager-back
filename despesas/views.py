from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from despesas.serializers import DespesaSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Despesa

class DespesaView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = DespesaSerializer
    queryset = Despesa.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DespesaDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = DespesaSerializer
    queryset = Despesa.objects.all()
    lookup_url_kwarg = "despesa_id"
