from rest_framework import serializers
from .models import Paciente, Profissional, Consulta, Pagamento, Prontuario, ContatoSuporte, PlanoAlimentar

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'


class ListaConsultasPacienteSerializer(serializers.ModelSerializer):
    paciente = serializers.ReadOnlyField(source='paciente.nome')
    profissional = serializers.ReadOnlyField(source='profissional.nome')
    data = serializers.DateField()
    horario = serializers.TimeField()

    class Meta:
        model = Consulta
        fields = ['paciente', 'profissional', 'data', 'horario']


class ListaConsultasProfissionalSerializer(serializers.ModelSerializer):
    paciente = serializers.ReadOnlyField(source='paciente.nome')
    data = serializers.DateField()
    horario = serializers.TimeField()

    class Meta:
        model = Consulta
        fields = ['paciente', 'data', 'horario']


class ProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prontuario
        fields = '__all__'


class ContatoSuporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoSuporte
        fields = '__all__'


class PlanoAlimentarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoAlimentar
        fields = '__all__'