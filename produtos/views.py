from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def Produtos_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})


def Produtos_new(request):
    form = ProdutoForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos/produto_form.html', {'form': form})


def Produtos_update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos/produto_form.html', {'form': form})


def Produtos_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos_list')
    return render(request, 'produtos/produto_delete_confirmation.html', {'produto': produto})
