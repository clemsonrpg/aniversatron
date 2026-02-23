from django.urls import path, include
from . import views

app_name = 'apps.core'
urlpatterns = [
    path('', views.index, name="index"),
    path('relatorios/', views.relatorios, name="relatorio"),
    path("relatorio/excel/", views.relatorio_excel, name="relatorio_excel")
]