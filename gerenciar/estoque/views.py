from django.shortcuts import render
from .models import Estoque

# Create your views here.
def estoque_entrada_list(request):
    template_nome = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request, template_nome, context)