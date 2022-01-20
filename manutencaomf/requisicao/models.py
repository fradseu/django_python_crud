from turtle import title
from django.db import models

# Create your models here.

# Dados para requisição/criação da ordem de manutenção

class Factory(models.Model):
    title = models.CharField(max_length=12)

    #função para nomear os itens que vem da bd
    # self pois se não nomear fica como item 1, item 2, item 3 e por ai vai. 
    def __str__(self):
        return self.title

class Solicitacao(models.Model):
    fullname = models.CharField(max_length=30)
    factory = models.ForeignKey(Factory, on_delete= models.CASCADE)
    machine_code = models.CharField(max_length=50)
    sector = models.CharField(max_length=12)
    priority_type = models.CharField(max_length= 12)
    date_create = models.DateField(auto_now_add=True)
    hour_arrive = models.TimeField(auto_now_add=True)
    issue_description = models.CharField(max_length= 150)