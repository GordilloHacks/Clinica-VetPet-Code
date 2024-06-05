from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def panel_inicio(request):
    return render(request, 'Panel.html')

def registro_inicio(request):
    return render(request, 'Registro.html')

def recu_contra(request):
    return render(request, 'Recu.html')

def Condiciones(request):
    return render(request, 'Condiciones.html')    