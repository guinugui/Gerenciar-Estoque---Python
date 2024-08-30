from django.urls import path
from gerenciar.core import views as v


app_name = 'core' #esse nome e chamado la no urls do gerenciar

urlpatterns = [
    path('', v.index, name='index'),
]
