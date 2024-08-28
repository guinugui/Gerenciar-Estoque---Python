from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    #atualiza data somente quando criar alguma coisa
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    #atualiza a data quando modifica o registro
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )
    class Meta:
        abstract = True