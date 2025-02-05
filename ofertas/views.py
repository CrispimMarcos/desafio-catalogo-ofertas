from django.shortcuts import render
from .models import Produto
from django.http import JsonResponse

def listar_produtos(request):
    produtos = Produto.objects.all()
    if 'frete_gratis' in request.GET:
        produtos = produtos.filter(frete_gratis=True)
    if 'full' in request.GET:
        produtos = produtos.filter(tipo_entrega='Full')
    
    context = {
        'produtos': produtos,
        'maior_preco': produtos.order_by('-preco').first(),
        'menor_preco': produtos.order_by('preco').first(),
        'maior_desconto': produtos.order_by('-percentual_desconto').first(),
    }
    return render(request, 'listar_produtos.html', context)

def listas_produtos_json(request):
    produtos = Produto.objects.all()
    if 'frete_gratis' in request.GET:
        produtos = produtos.filter(frete_gratis=True)
    if 'full' in request.GET:
        produtos = produtos.filter(tipo_entrega='Full')
    
    produtos = list(produtos.values())
    return JsonResponse(produtos, safe=False)
