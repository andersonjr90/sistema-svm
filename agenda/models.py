from django.db import models


class Agendamento(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    assunto = models.CharField(max_length=45)
    prioridade = models.CharField(max_length=45)
    duracao = models.IntegerField()
    agendamento_id_tripulante = models.ForeignKey('Tripulante', models.DO_NOTHING, db_column='agendamento_id_tripulante')

    class Meta:
        db_table = 'agendamento'


class Compromisso(models.Model):
    id_compromisso = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=45)
    data = models.DateField()
    rotina = models.SmallIntegerField()
    horario = models.DateTimeField()

    class Meta:
        db_table = 'compromisso'


class FilaEspera(models.Model):
    id_fila_espera = models.AutoField(primary_key=True)
    agendamento_id_agendamento = models.ForeignKey(Agendamento, models.DO_NOTHING, db_column='agendamento_id_agendamento')
    atendido = models.SmallIntegerField()

    class Meta:
        db_table = 'fila_espera'


class QuadroTarefas(models.Model):
    tarefa_id_tarefa = models.OneToOneField('Tarefa', models.DO_NOTHING, db_column='tarefa_id_tarefa', primary_key=True)
    compromisso_id_compromisso = models.ForeignKey(Compromisso, models.DO_NOTHING, db_column='compromisso_id_compromisso')

    class Meta:
        db_table = 'quadro_tarefas'
        unique_together = (('tarefa_id_tarefa', 'compromisso_id_compromisso'),)


class Tarefa(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=450)

    class Meta:
        db_table = 'tarefa'


class TarefaTripulante(models.Model):
    tarefa_id_tarefa = models.OneToOneField(Tarefa, models.DO_NOTHING, db_column='tarefa_id_tarefa', primary_key=True)
    tripulante_id_tripulante = models.ForeignKey('Tripulante', models.DO_NOTHING, db_column='tripulante_id_tripulante')

    class Meta:
        db_table = 'tarefa_tripulante'
        unique_together = (('tarefa_id_tarefa', 'tripulante_id_tripulante'),)


class Tripulante(models.Model):
    id_tripulante = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=300)
    contato = models.CharField(max_length=45)
    dt_nasc = models.DateField()
    setor = models.CharField(max_length=100)
    militar = models.SmallIntegerField()
    patente = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'tripulante'

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=300)
    senha = models.CharField(max_length=200)
    permissao = models.CharField(max_length=45)
    tipo_usuario = models.CharField(max_length=45)

    class Meta:
        db_table = 'usuario'
