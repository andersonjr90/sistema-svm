from django.contrib import admin

from .models import (
  Agendamento, Compromisso, FilaEspera, QuadroTarefas, Tarefa,
  Tripulante,
  TarefaTripulante,
  Usuario
)


class AgendamentoAdmin(admin.ModelAdmin):  
    list_display = ('id_agendamento', 'assunto', 'prioridade', 'duracao') 
    

class CompromissoAdmin(admin.ModelAdmin):  
    list_display = ('id_compromisso','descricao','data', 'rotina','horario')


class FilaEsperaAdmin(admin.ModelAdmin):  
    list_display = ('id_fila_espera', 'agendamento_id_agendamento', 'atendido')


class QuadroTarefasAdmin(admin.ModelAdmin):  
    list_display = ('tarefa_id_tarefa', 'compromisso_id_compromisso')


class TarefaAdmin(admin.ModelAdmin):  
    list_display = ('id_tarefa', 'descricao')


class TarefaTripulanteAdmin(admin.ModelAdmin):
    list_display = ('tarefa_id_tarefa', 'tripulante_id_tripulante')


class TripulanteAdmin(admin.ModelAdmin):  
    list_display = ('id_tripulante', 'nome', 'contato', 'dt_nasc', 'setor',
                    'militar', 'patente')


class UsuarioAdmin(admin.ModelAdmin):  
    list_display = ('id_usuario', 'email', 'nome', 'senha', 'permissao',
                    'tipo_usuario')


# Register your models here.
admin.site.register(Agendamento, AgendamentoAdmin)  
admin.site.register(Compromisso, CompromissoAdmin)
admin.site.register(FilaEspera, FilaEsperaAdmin)
admin.site.register(QuadroTarefas, QuadroTarefasAdmin)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Tripulante, TripulanteAdmin)
admin.site.register(TarefaTripulante, TarefaTripulanteAdmin)
admin.site.register(Usuario, UsuarioAdmin)
