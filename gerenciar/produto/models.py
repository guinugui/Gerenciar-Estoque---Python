from django.contrib import admin
from django.db import models
from django.urls import reverse_lazy

# Create your models here.
# Ele gera uma tabela criando uma arquivo dessas tabela criadas. basta aplicar esses comando abaixo 
# python manage.py makemigrations
#python manage.py migrate 
class Produto (models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    produto = models.CharField(max_length= 100, unique=True)
    preco = models.DecimalField('preço', max_digits = 7, decimal_places= 2, default = 0)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveBigIntegerField('estoque mínimo', default= 0)
    
    class Meta():
        ordering = ('produto',)
        
    def __str__(self) -> str:
        return self.produto
    
    def get_absolute_url(self):
        return reverse_lazy("produto:produto_detail", kwargs={"pk": self.pk}) #esse codigo e para a urls para renderizar o produto detalhes em qualquer lugar usando object.get_absolute_url
    