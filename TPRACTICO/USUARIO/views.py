from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .forms import *

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()          
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form
        })

def buscar(request):
    return render(request, 'buscar/search.html')

def layout(request):
    return render(request, 'registration/layout.html')

def home(request):
    return render(request, 'index/home.html')

def categories(request):
    return render(request, 'categorias/categories.html')
    
def contact(request):
    return render(request, 'index/contact.html')

def about(request):
    return render(request, 'index/about.html')

def category1(request):
    return render(request, 'categorias/category1.html')

def category2(request):
    return render(request, 'categorias/category2.html')

def category3(request):
    return render(request, 'categorias/category3.html')

def product1(request):
    return render(request, 'productos/product1.html')

def product2(request):
    return render(request, 'productos/product2.html')

def product3(request):
    return render(request, 'productos/product3.html')

def product4(request):
    return render(request, 'productos/product4.html')

def product5(request):
    return render(request, 'productos/product5.html')

def product6(request):
    return render(request, 'productos/product6.html')

def product7(request):
    return render(request, 'productos/product7.html')

def product8(request):
    return render(request, 'productos/product8.html')

def product9(request):
    return render(request, 'productos/product9.html')

def product10(request):
    return render(request, 'productos/product10.html')