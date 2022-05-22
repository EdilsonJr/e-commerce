from django.urls import path
from . import views


app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('addaocarinnho/', views.AddAoCarrinho.as_view(), name='addaocarinnho'),
    path('removerdocarinnho/', views.RemoverDoCarrinho.as_view(), name='removerdocarinnho'),
    path('carinnho/', views.Carrinho.as_view(), name='carinnho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
]