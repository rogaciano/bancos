from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('bancos/', views.banco_list, name='banco_list'),
    path('bancos/novo/', views.banco_create, name='banco_create'),
    path('bancos/<int:pk>/editar/', views.banco_update, name='banco_update'),
    path('bancos/<int:banco_id>/movimentacoes/', views.movimentacao_list, name='movimentacao_list'),
    path('bancos/<int:banco_id>/movimentacoes/nova/', views.movimentacao_create, name='movimentacao_create'),
]
