from django.db import models

class Generos(models.Model):
    genero = models.CharField('Gênero', max_length=100)

    def __str__(self) -> str:
        return self.genero

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

class Filmes(models.Model):
    filme = models.CharField('Nome', max_length=100)
    genero = models.ForeignKey(Generos, on_delete=models.PROTECT)
    quantidade = models.IntegerField('Quantidade', default=0)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    # def __str__(self) -> str:
    #     return self.filme

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'