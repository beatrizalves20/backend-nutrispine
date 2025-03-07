from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Paciente, Profissional, Consulta, Pagamento, Prontuario, ContatoSuporte, PlanoAlimentar
from . import serializers

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer


class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = serializers.ProfissionalSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = serializers.ConsultaSerializer


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = serializers.PagamentoSerializer


class ListaConsultasPaciente(generics.ListAPIView):
    serializer_class = serializers.ListaConsultasPacienteSerializer

    def get_queryset(self):
        queryset = Consulta.objects.filter(paciente_id=self.kwargs['pk'])
        return queryset
    

class ListaConsultasProfissional(generics.ListAPIView):
    serializer_class = serializers.ListaConsultasProfissionalSerializer

    def get_queryset(self):
        return Consulta.objects.filter(profissional_id=self.kwargs['pk'])
    

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = serializers.ProntuarioSerializer


class ContatoSuporteViewSet(viewsets.ModelViewSet):
    queryset = ContatoSuporte.objects.all()
    serializer_class = serializers.ContatoSuporteSerializer


class PlanoAlimentarViewSet(viewsets.ModelViewSet):
    queryset = PlanoAlimentar.objects.all()
    serializer_class = serializers.PlanoAlimentarSerializer