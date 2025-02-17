from django.db import models
from django.db.models import Sum

class Banco(models.Model):
    nome = models.CharField(max_length=100)
    numero_conta = models.CharField(max_length=20)
    nome_gerente = models.CharField(max_length=100)
    contato_gerente = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def saldo_atual(self):
        creditos = self.movimentacoes.filter(tipo='C').aggregate(total=Sum('valor'))['total'] or 0
        debitos = self.movimentacoes.filter(tipo='D').aggregate(total=Sum('valor'))['total'] or 0
        return creditos - debitos

    def __str__(self):
        return f"{self.nome} - {self.numero_conta}"

    class Meta:
        verbose_name = 'Conta Bancária'
        verbose_name_plural = 'Contas Bancárias'

class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('C', 'Crédito'),
        ('D', 'Débito'),
    ]

    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, related_name='movimentacoes')
    data = models.DateField()
    documento = models.CharField(max_length=50)
    descricao = models.TextField()
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False, null=False)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.data} - {self.descricao} - {self.valor}"

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'
        ordering = ['-data', '-data_cadastro']
