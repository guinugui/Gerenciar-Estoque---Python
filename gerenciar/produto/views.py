from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm


# Create your views here.
def produto_list(request):  #aqui cria um lista dos objetos de produtos
    template_name = 'produto_list.html'
    object = Produto.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk) # essa linha ele faz um get pega o id daquele produto que foi clicado e salva em ojs
    context = {'object': obj}
    return render(request, template_name, context)

def produto_add(request):
    template_name = 'produto_form.html' # aqui é pra tenderizar
    return render(request, template_name)


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm #classe la do html que vincula que faz criar algum produto
    
class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm 