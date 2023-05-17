from django.urls import path
from Site import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.produto.lista, name='produto_lista'),
    path('produto', views.produto_detalhe, name= 'produto_detalhe')
]