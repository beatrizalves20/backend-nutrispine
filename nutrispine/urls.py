from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('pacientes', views.PacienteViewSet, basename='pacientes')
router.register('profissionais', views.ProfissionalViewSet, basename='profissionais')
router.register('consultas', views.ConsultaViewSet, basename='consultas')
router.register('pagamentos', views.PagamentoViewSet, basename='pagamentos')
router.register('prontuarios', views.ProntuarioViewSet, basename='prontuario')
router.register('contatos', views.ContatoSuporteViewSet, basename='contatos')
router.register('planos_alimentares', views.PlanoAlimentarViewSet, basename='planos_alimentares')

urlpatterns = [
    path('', include(router.urls)),
    path('pacientes/<int:pk>/consultas/', views.ListaConsultasPaciente.as_view(), name='lista-consultas-paciente'),
    path('profissionais/<int:pk>/consultas/', views.ListaConsultasProfissional.as_view(), name='lista-consultas-profissional'),
]