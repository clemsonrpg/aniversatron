from django.urls import path

from apps.servicos import views

app_name = 'apps.servicos'

urlpatterns = [
    path('inserir_servico/', views.inserir_servico, name='inserir_servico'),
    path('listar_servicos/', views.listar_servicos, name='listar_servicos'),
    path('editar_servico/<int:id>/', views.editar_servico, name='editar_servico'),
    path('excluir_servico/<int:id>/', views.excluir_servico, name='excluir_servico'),
    path('detalhe_servico/<int:id>/', views.detalhe_servico, name='detalhe_servico'),
]