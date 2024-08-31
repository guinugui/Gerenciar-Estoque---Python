from django.contrib.auth.models import User
from django.db import models
from gerenciar.core.models import TimeStampedModel
from gerenciar.produto.models import Produto
from django.db import models

# Create your models here.
MOVIMENTO = [
    ('e', 'entrada'),
    ('s', 'saida'),
]

class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length= 1, choices=MOVIMENTO) # Ele mostra que entra e sai
    
    class Meta():
        ordering = ('-created',)
        
    def __str__(self) -> str:
        return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
    
    def nf_formated(self):
        return str(self.nf).zfill(3) # coloca o 0 a esquerda do numero mas tem que ser string
    
class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField()
    saldo = models.PositiveIntegerField()
    
    class Meta:
        ordering = ('pk',)
        
    def __str__(self) -> str:
        return '{}---{}---{}'.format(self.pk, self.estoque.pk, self.produto)