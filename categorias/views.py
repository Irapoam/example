#coding: utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse as r
from django.http import HttpResponseRedirect

from .models import Categoria
from .forms import CategoriaForm


def home(request):
	return render(request, "home.html")

def lista_categorias(request):
	return render(request, "categorias/lista.html", {'categorias':Categoria.objects.all()})

def nova_categoria(request):
	#verifica o tipo de requisição
	if request.method == 'POST':
		#caso seja post, pega os dados enviados
		form = CategoriaForm(request.POST)
		#se o form for válido, salva e retorna para a lista
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(r('categorias:lista_categorias'))
		else:
			#se for inválido retorna para a tela exibindo os erros
			return render(request, 'categorias/categoria_nova.html',{'form':form })	
	else:
		return render(request, 'categorias/categoria_nova.html',{'form':CategoriaForm()})

def editar_categoria(request, pk):
	categoria = Categoria.objects.get(pk=pk)
	if request.method == 'POST':
		form = CategoriaForm(request.POST, instance=categoria)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(r('categorias:lista_categorias'))
		else:
			return render(request, 'categorias/categoria_editar.html',{'form':form })	
	else:
		return render(request, 'categorias/categoria_editar.html',{'form':CategoriaForm(instance=categoria)})
