from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=50)
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categorias'
        ordering = ('id',)

    def __str__(self):
        return self.name
