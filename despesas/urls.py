from django.urls import path

from . import views

urlpatterns = [
    path("despesas", views.DespesaView.as_view()),
    path("despesas/<uuid:despesa_id>", views.DespesaDetailView.as_view()),
]
