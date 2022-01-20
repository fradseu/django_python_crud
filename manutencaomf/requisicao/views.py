from contextlib import redirect_stderr
from multiprocessing import context

from django.shortcuts import redirect, render

#from manutencaomf import requisicao

from .forms import requisicaoForm
from .models import Solicitacao

# Create your views here.



def requisicao_list(request):
    context = {'requisicao_list': Solicitacao.objects.all()}
    return render(request,"requisicao_register/requisicao_list.html",context)

def requisicao_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = requisicaoForm()
        else:
            requisicao = Solicitacao.objects.get(pk=id)
            form = requisicaoForm(instance=requisicao)
        return render(request,"requisicao_register/requisicao_form.html",{'form':form})
    else:
        if id ==0 :
            form = requisicaoForm(request.POST)
        else:
            requisicao = Solicitacao.objects.get(pk=id)
            form = requisicaoForm(request.POST,instance =requisicao)
        if form.is_valid():
            form.save()
        return redirect('/requisicao/list')

def requisicao_delete(request,id):
    requisicao = Solicitacao.objects.get(pk=id)
    requisicao.delete()
    return redirect ('/requisicao/list')

