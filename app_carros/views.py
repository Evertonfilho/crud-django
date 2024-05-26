from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from app_carros.models import Carro

def home(request):
    return render(request,'carros/index.html')

def lista_carros(request):
    novo_carro = Carro()
    novo_carro.modelo = request.POST.get('modelo')
    novo_carro.quantidade_portas = request.POST.get('portas')
    novo_carro.tipo_combustivel = request.POST.get('combustivel')
    novo_carro.ano_carro = request.POST.get('ano')
    novo_carro.placa = request.POST.get('placa')
    novo_carro.estado = request.POST.get('estado')
    novo_carro.valor_comprado = request.POST.get('valor_comprado')
    novo_carro.valor_vendido = request.POST.get('valor_vendido')
    novo_carro.save()
    carros ={
        'carros': Carro.objects.all()
    }
    return render(request,'carros/lista/index.html',carros) 

def mostrar_lista(request):
    carros ={
        'carros': Carro.objects.all()
    }
    return render(request,'carros/lista/index.html',carros) 

def editar_carro(request, id):
    try:
        carroExistente = Carro.objects.get(id_carro=id)
    except Carro.DoesNotExist:
        context = {'error_message': 'Carro não encontrado.'}
        return render(request, 'carros/lista/index.html', Carro.objects.all())
    
    if request.method == 'POST':
        carroExistente.modelo = request.POST.get('modelo')
        carroExistente.quantidade_portas = request.POST.get('quantidade_portas')
        carroExistente.tipo_combustivel = request.POST.get('tipo_combustivel')
        carroExistente.ano_carro = request.POST.get('ano_carro')
        carroExistente.placa = request.POST.get('placa')
        carroExistente.estado = request.POST.get('estado')
        carroExistente.valor_comprado = request.POST.get('valor_comprado')
        carroExistente.valor_vendido = request.POST.get('valor_vendido')
        carroExistente.save()
        return redirect('mostrar_lista')

    context = {
        'carro': carroExistente
    }
    return render(request, 'carros/editar/index.html', context)

def deletar_carro(request, id):
    try:
        carro = Carro.objects.get(id_carro=id)
    except Carro.DoesNotExist:
        context = {'error_message': 'Carro não encontrado.'}
        return render(request, 'carros/lista/index.html', context)

    if request.method == 'POST':
        carro.delete()
        return redirect('mostrar_lista')
    
    context = {
        'carro': carro
    }
    return render(request, 'carros/deletar/index.html', context)