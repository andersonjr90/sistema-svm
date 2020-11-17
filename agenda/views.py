from datetime import datetime

import jwt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from tcc.settings import SECRET_KEY
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
    serializer_class = TarefaSerializer
    queryset = Tarefa.objects.all()


class TarefaTripulanteView(viewsets.ModelViewSet):
    serializer_class = TarefaTripulanteSerializer
    queryset = TarefaTripulante.objects.all()


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = LoginSerializer(data)
        email = serializer.data['email']
        senha = serializer.data['senha']
        if Usuario.objects.filter(email=email).exists():
            usuario = Usuario.objects.get(email=email)
            if usuario.senha == senha:
                payload = {
                    'id_usuario': usuario.id_usuario,
                    'email': email,
                    'tipo_usuario': usuario.tipo_usuario,
                    'permissao': usuario.permissao,
                    'exp': datetime.now(),
                    'token_type': 'access'
                }

                token = jwt.encode(payload, SECRET_KEY).decode('utf-8')
                return Response(
                    {'success': 'true', 'token': token, 'tipo_usuario':
                        usuario.tipo_usuario}
                )

        return Response(
            {'success': 'false', 'msg': 'The credentials provided are invalid.'}
        )
