from django.urls import path
from app_carros import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carros/', views.lista_carros, name='lista_carros'),
    path('carros/lista', views.mostrar_lista, name='mostrar_lista'),
    path('editar/<int:id>/', views.editar_carro, name='editar_carro'),
    path('deletar/<int:id>/', views.deletar_carro, name='deletar_carro'),
]
