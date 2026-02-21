from django.urls import path
from . import views


app_name = 'apps.pessoas'

urlpatterns = [
    path('inserir_pessoa/', views.inserir_pessoa, name='inserir_pessoa'),
    path('listar_pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('editar_pessoa/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('excluir_pessoa/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),
]