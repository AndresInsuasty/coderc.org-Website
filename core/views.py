from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/index.html")

def asesoria(request):
    return render(request,"core/asesoria.html")

def capacitacion(request):
    return render(request,"core/capacitacion.html")
    
def about(request):
    return render(request, "core/about.html")

def contacto(request):
    return render(request, "core/contacto.html")