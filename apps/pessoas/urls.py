from django.urls import path
from . import views


app_name = 'apps.pessoas'

urlpatterns = [
    path('inserir_pessoa/', views.inserir_pessoa, name='inserir_pessoa'),
    path('listar_pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('editar_pessoa/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('excluir_pessoa/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),
    path('detalhe_pessoa/<int:id>/', views.detalhe_pessoa, name='detalhe_pessoa'),
    path('inserir_propriedade/<int:pessoa_id>/', views.inserir_propriedade, name='inserir_propriedade')
    ]