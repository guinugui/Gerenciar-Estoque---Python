from django.shortcuts import render
from .models import Produto

# Create your views here.
def produto_list(request):
    template_name = 'produto_list.html'
    object = Produto.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)