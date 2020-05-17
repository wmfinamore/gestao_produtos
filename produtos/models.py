from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    descricao = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='foto_produtos', null=True, blank=True)

    def __str__(self):
        return self.nome
