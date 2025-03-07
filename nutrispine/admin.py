from django.contrib import admin
from .models import Paciente, Profissional, Consulta, Pagamento, Prontuario, ContatoSuporte, PlanoAlimentar

@admin.register(Paciente)
class Pacientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'telefone')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome',)


@admin.register(Profissional)
class Profissionais(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'telefone', 'especialidade', 'registro')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome',)


@admin.register(Consulta)
class Consultas(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'email', 'data', 'horario', 'profissional')
    list_display_links = ('id', 'paciente', 'profissional')
    list_per_page = 20
    search_fields = ('paciente', 'profissional')


@admin.register(Pagamento)
class Pagamentos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'valor')
    list_display_links = ('id', 'nome', 'cpf')
    list_per_page = 20
    search_fields = ('nome', 'cpf')


@admin.register(Prontuario)
class Prontuarios(admin.ModelAdmin):
    list_display = ('id', 'paciente')
    list_display_links = ('id', 'paciente')
    list_per_page = 20
    search_fields = ('paciente',)


@admin.register(ContatoSuporte)
class ContatoSuporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome',)


@admin.register(PlanoAlimentar)
class PlanoAlimentarAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome', 'cpf', 'email',)