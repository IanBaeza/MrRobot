from django.shortcuts import render
from django.utils import timezone
from .models import Computador
from django.shortcuts import redirect

# Create your views here.

def index(request):
	return render(request,'mrrobotin/index.html')

def inicio(request):
	return render(request,'mrrobotin/inicio.html')	

def galeria(request):
	return render(request,'mrrobotin/galeria.html')

def pc(request):
	return render(request,'mrrobotin/pc.html')

def registro(request):
	return render(request,'mrrobotin/registro.html')