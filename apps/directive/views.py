from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request, 'products.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def index(request):
    return render(request, 'index.html', {})

def presentation(request):
    return render(request, 'type_cafe/presentation/coffee_presentation.html', {})

