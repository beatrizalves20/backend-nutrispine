from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    especialidade = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} - {self.registro}'
    

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True, null=True, max_length=100)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f'Paciente: {self.paciente.nome} - Profissional: {self.profissional.nome}'
    

class Pagamento(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    numero_cartao = models.CharField(max_length=100)
    data_validade = models.DateField()
    cvv = models.IntegerField()
    valor = models.FloatField()


class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    # profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    diasgnostico = models.TextField()
    tratamento = models.TextField()
    recomendacoes = models.TextField()


class ContatoSuporte(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True, max_length=100)
    telefone = models.CharField(max_length=14)
    mensagem = models.TextField()

    class Meta:
        verbose_name_plural = 'Contatos Suportes'


class PlanoAlimentar(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(blank=True, null=True, max_length=100)
    telefone = models.CharField(max_length=14)
    plano_alimentar = models.TextField(null=True, blank=True)
    tratamento_personalizado = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Planos Alimentares'