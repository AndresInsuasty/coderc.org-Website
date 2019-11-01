from django.shortcuts import render
from .models import Project

# Create your views here.
def comproagro(request):
    projects = Project.objects.all()
    return render(request,"comproagro/comproagro.html",{'projects':projects})