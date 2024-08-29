from django.urls import path
from gerenciar.produto import views as v


app_name = 'produto'


urlpatterns = [
    path('', v.produto_list, name='produto_list'), #renderiza os produtos
    path('<int:pk>', v.produto_detail, name='produto_detail'),#renderiza o detalhe do produto
    path('add/', v.produto_add, name='produto_add')#renderiza o template de adicionar um produto
    
]
