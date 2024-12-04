from django.urls import path
from . import views

urlpatterns = [
    path('', views.logar, name='logar'),
    path('sair/', views.sair, name='sair'),
    path('prontoarios/', views.prontuario_list, name='prontuario_list'),
    path('prontuarios/<int:pk>/', views.prontuario_detail, name='prontuario_detail'),
    path('prontuarios/new/', views.prontuario_create, name='prontuario_create'),
    path('prontuarios/<int:pk>/edit/', views.prontuario_update, name='prontuario_update'),
    path('prontuarios/<int:pk>/delete/', views.prontuario_delete, name='prontuario_delete'),
]