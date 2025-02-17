from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from .models import Banco, Movimentacao
from .forms import BancoForm, MovimentacaoForm

def dashboard(request):
    bancos = Banco.objects.all()
    saldo_geral = sum(banco.saldo_atual() for banco in bancos)
    
    context = {
        'bancos': bancos,
        'saldo_geral': saldo_geral,
    }
    return render(request, 'bancos/dashboard.html', context)

def banco_list(request):
    bancos = Banco.objects.all()
    return render(request, 'bancos/banco_list.html', {'bancos': bancos})

def banco_create(request):
    if request.method == 'POST':
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta bancária cadastrada com sucesso!')
            return redirect('banco_list')
    else:
        form = BancoForm()
    return render(request, 'bancos/banco_form.html', {'form': form})

def banco_update(request, pk):
    banco = get_object_or_404(Banco, pk=pk)
    if request.method == 'POST':
        form = BancoForm(request.POST, instance=banco)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta bancária atualizada com sucesso!')
            return redirect('banco_list')
    else:
        form = BancoForm(instance=banco)
    return render(request, 'bancos/banco_form.html', {'form': form})

def movimentacao_list(request, banco_id):
    banco = get_object_or_404(Banco, pk=banco_id)
    movimentacoes = banco.movimentacoes.all()
    return render(request, 'bancos/movimentacao_list.html', {
        'banco': banco,
        'movimentacoes': movimentacoes
    })

def movimentacao_create(request, banco_id):
    banco = get_object_or_404(Banco, pk=banco_id)
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.banco = banco
            movimentacao.save()
            messages.success(request, 'Movimentação registrada com sucesso!')
            return redirect('movimentacao_list', banco_id=banco.id)
    else:
        form = MovimentacaoForm()
    return render(request, 'bancos/movimentacao_form.html', {
        'form': form,
        'banco': banco
    })
