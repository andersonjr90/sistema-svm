from rest_framework import viewsets

from .serializers import *


class TripulanteView(viewsets.ModelViewSet):  # add this
    serializer_class = TripulanteSerializer  # add this
    queryset = Tripulante.objects.all()


class AgendamentoView(viewsets.ModelViewSet):
    serializer_class = AgendamentoSerializer
    queryset = Agendamento.objects.all()


class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class CompromissoView(viewsets.ModelViewSet):
    serializer_class = CompromissoSerializer  # add this
    queryset = Compromisso.objects.all()


class FilaEsperaView(viewsets.ModelViewSet):
    serializer_class = FilaEsperaSerializer  # add this
    queryset = FilaEspera.objects.all()


class QuadroTarefasView(viewsets.ModelViewSet):
    serializer_class = QuadroTarefasSerializer
    queryset = QuadroTarefas.objects.all()


class TarefaView(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer  # add this
    queryset = Tarefa.objects.all()


class TarefaTripulanteView(viewsets.ModelViewSet):
    serializer_class = TarefaTripulanteSerializer
    queryset = TarefaTripulante.objects.all()
