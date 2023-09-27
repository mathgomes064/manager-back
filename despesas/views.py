from django.shortcuts import render
from despesas.serializer import DespesaSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Despesa

class DespesaView(ListCreateAPIView):
    serializer_class = DespesaSerializer
    queryset = Despesa.objects.all()

class DespesaDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DespesaSerializer
    queryset = Despesa.objects.all()
    lookup_url_kwarg = "despesa_id"
