from rest_framework import serializers
from .models import (
    Agendamento, Compromisso, FilaEspera, QuadroTarefas,
    Tarefa, TarefaTripulante, Tripulante, Usuario
)


class TripulanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tripulante
        fields = ('id_tripulante', 'nome', 'contato', 'dt_nasc', 'setor',
                  'militar', 'patente')


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id_usuario', 'email', 'nome', 'senha', 'permissao',
                  'tipo_usuario')


class AgendamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento
        fields = ('id_agendamento', 'assunto', 'prioridade', 'duracao',
                  'agendamento_id_tripulante')


class CompromissoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compromisso
        fields = ('id_compromisso', 'descricao', 'data', 'rotina', 'horario')


class FilaEsperaSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilaEspera
        fields = ('id_fila_espera', 'agendamento_id_agendamento', 'atendido')


class QuadroTarefasSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuadroTarefas
        fields = ('tarefa_id_tarefa', 'compromisso_id_compromisso')


class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarefa
        fields = ('id_tarefa', 'descricao')


class TarefaTripulanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = TarefaTripulante
        fields = ('tarefa_id_tarefa', 'tripulante_id_tripulante')

