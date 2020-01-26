from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=150)
    description = models.TextField(
        verbose_name='Descrição', null=True, blank=True)
    owner = models.ForeignKey(
        User, verbose_name='Dono', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categoria'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )

    STATUS_CHOICES = (
        ('EX', 'Em execução'),
        ('PD', 'Pendente'),
        ('CD', 'Concluída'),
    )

    name = models.CharField(verbose_name='Tarefa', max_length=200)
    description = models.TextField(
        verbose_name='Descrição', blank=True, null=True)
    end_date = models.DateField(verbose_name='Data final')
    priority = models.CharField(
        verbose_name='Prioridade', max_length=1, choices=PRIORITY_CHOICES)
    category = models.ManyToManyField(Category, verbose_name='Categoria')
    status = models.CharField(verbose_name='Status',
                              max_length=2, choices=STATUS_CHOICES)
    owner = models.ForeignKey(
        User, verbose_name='Dono', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tarefa'
        ordering = ('end_date',)

    def __str__(self):
        return self.name
