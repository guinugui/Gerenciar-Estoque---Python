from django.db import models

# Create your models here.
# Ele gera uma tabela criando uma arquivo dessas tabela criadas. basta aplicar esses comando abaixo 
# python manage.py makemigrations
#python manage.py migrate 
class Produto (models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    produto = models.CharField(max_length= 100, unique=True)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveBigIntegerField('estoque mínimo', default= 0)
    
    class Meta():
        ordering = ('produto',)
        
    def __str__(self) -> str:
        return self.produto