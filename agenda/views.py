from datetime import datetime

import jwt
from django.contrib.auth.hashers import check_password, make_password
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
    permission_classes = [AllowAny]


class AgendamentoView(viewsets.ModelViewSet):
    serializer_class = AgendamentoSerializer
    queryset = Agendamento.objects.all()
    permission_classes = [AllowAny]


class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(senha=make_password(serializer.validated_data['senha']))


class CompromissoView(viewsets.ModelViewSet):
    serializer_class = CompromissoSerializer
    queryset = Compromisso.objects.all()
    permission_classes = [AllowAny]


class FilaEsperaView(viewsets.ModelViewSet):
    serializer_class = FilaEsperaSerializer
    queryset = FilaEspera.objects.all()
    permission_classes = [AllowAny]


class QuadroTarefasView(viewsets.ModelViewSet):
    serializer_class = QuadroTarefasSerializer
    queryset = QuadroTarefas.objects.all()
    permission_classes = [AllowAny]


class TarefaView(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    queryset = Tarefa.objects.all()
    permission_classes = [AllowAny]


class TarefaTripulanteView(viewsets.ModelViewSet):
    serializer_class = TarefaTripulanteSerializer
    queryset = TarefaTripulante.objects.all()
    permission_classes = [AllowAny]


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = LoginSerializer(data)
        email = serializer.data['email']
        senha = serializer.data['senha']
        if Usuario.objects.filter(email=email).exists():
            usuario = Usuario.objects.get(email=email)

            if check_password(senha, usuario.senha):
                payload = {
                    'id_usuario': usuario.id_usuario,
                    'email': email,
                    'tipo_usuario': usuario.tipo_usuario,
                    'permissao': usuario.permissao,
                    'exp': datetime.now(),
                    'token_type': 'access'
                }
                user = {
                    'usuario': usuario.nome,
                    'email': email,
                    'tipo_usuario': usuario.tipo_usuario,
                    'permissao': usuario.permissao
                }

                token = jwt.encode(payload, SECRET_KEY).decode('utf-8')
                return Response(
                    {'success': 'true', 'token': token, 'user': user}
                )

        return Response(
            {'success': 'false', 'msg': 'Credenciais inválidas'}
        )
