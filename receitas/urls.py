from django.urls import path

from . import views

urlpatterns = [
    path("receitas", views.ReceitaView.as_view()),
    path("receitas/<uuid:receita_id>", views.ReceitaDetailView.as_view()),
]
