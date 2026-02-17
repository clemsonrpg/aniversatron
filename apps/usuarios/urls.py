from django.urls import path
from apps.usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('inserir_usuario/', views.inserir_usuario, name='inserir_usuario'),
    path('login/', views.login, name='login'),
    path('sair/', views.logout, name='logout'),
]