from django.db import models

# Create your models here.

class Prontuario(models.Model):

    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viuvo', 'Viúvo'),
    ]

    SENSIBILIDADE_ANESTESIA_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

    SENSIBILIDADE_ANTIBIOTICOS_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=250)
    profissao = models.CharField(max_length=250)
    indicado_por = models.CharField(max_length=250)
    estado_civil = models.CharField(
        max_length=10,
        choices=ESTADO_CIVIL_CHOICES,
        default='solteiro',
    )
    inicio_tratamento = models.DateField()
    termino_tratamento = models.DateField(null=True, blank=True)
    interrupcao = models.DateField(null=True, blank=True)
    anotações = models.TextField()
    tc=models.DateTimeField()
    ts=models.DateTimeField()
    pa_max=models.PositiveIntegerField()
    pa_min=models.PositiveIntegerField()
    sensibilidade_anestisia = models.CharField(max_length=3, 
    choices=SENSIBILIDADE_ANESTESIA_CHOICES, default='sim'
    )
    sensibilidade_antibiotico = models.CharField(max_length=3,
    choices=SENSIBILIDADE_ANTIBIOTICOS_CHOICES, default='sim'
    )
    data = models.DateField()
    dente = models.CharField(max_length=10)
    tratamento_realidado = models.CharField(max_length=100)
    tempo = models.CharField(max_length=10)
    debito = models.CharField(max_length=10)
    credito = models.CharField(max_length=10)
    saldo = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.nome} - CPF: {self.cpf}'