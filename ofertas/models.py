from django.db import models

class Produto(models.Model):
    imagem = models.URLField()
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    parcelamento = models.CharField(max_length=255)
    link = models.URLField()
    preco_sem_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentual_desconto = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tipo_entrega = models.CharField(max_length=50)
    frete_gratis = models.BooleanField(default=False)
    db_table = 'ofertas_produto'

    def __str__(self):
        return self.nome
