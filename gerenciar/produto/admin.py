from django.contrib import admin
from .models import Produto
# Register your models here.
#esse produto vem lá da pasta produto models.py aquela classe 
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
# é o campo aonde aparece la na tela as colunas
    list_display= (
        '__str__',
        'importado',
        'ncm',
        'preco',
        'estoque',
        'estoque_minimo',
    )
    search_fields = ('produto',) # campo de busca
    list_filter = ('importado',) #  lista de filtrados na direita da tela
    