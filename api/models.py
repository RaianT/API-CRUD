from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)  # Ajuste o tamanho conforme necessário
    cep = models.CharField(max_length=10)        # Ajuste o tamanho conforme necessário
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
