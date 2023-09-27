from django.shortcuts import render
from receitas.serializers import ReceitaSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Receita

class ReceitaView(ListCreateAPIView):
    serializer_class = ReceitaSerializer
    queryset = Receita.objects.all()

class ReceitaDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReceitaSerializer
    queryset = Receita.objects.all()
    lookup_url_kwarg = "receita_id"
