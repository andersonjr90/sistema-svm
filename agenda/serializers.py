from rest_framework import serializers
from .models import Agendamento, Compromisso, FilaEspera, QuadroTarefas,
Tarefa, TarefaTripulante, Tripulante,Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id_usuario','senha', 'permissao', 'tipo_usuario', 'phone',
                  'address','description')