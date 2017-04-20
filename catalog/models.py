# coding=utf-8

from django.db import models


class Category(models.Model):                   # Criando os modelos que sao as nossas classes que representam as tabelas da nossa aplicacao catalogo

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)  #Pega a data de criacao
    modified = models.DateTimeField('Modificado em', auto_now=True) #Pega a data da ultima modificacao

    if __name__ == '__main__':
        class Meta:
            verbose_name = 'Categoria'
            verbose_name_plural = 'Categorias'
            ordering = ['name']

        # a saber: A categoria tem um ou mais produtos


class Product(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    # O relacionamento de um para n voce coloca no n porque eh ele que tem que referenciar como eho caso de category porque ele tem uma categoria associada
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)     #blank = em branco porque em bd nao existe nulo
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
