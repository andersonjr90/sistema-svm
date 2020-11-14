"""tcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from agenda import views

router = routers.DefaultRouter()                      # add this
router.register(r'tripulantes', views.TripulanteView, 'tripulante')
router.register(r'agendamentos', views.AgendamentoView, 'agendamento')
router.register(r'usuarios', views.UsuarioView, 'usuario')
router.register(r'compromissos', views.CompromissoView, 'compromisso')
router.register(r'filaespera', views.FilaEsperaView, 'filaespera')
router.register(r'quadrotarefas', views.QuadroTarefasView, 'quadrotarefas')
router.register(r'tarefas', views.TarefaView, 'tarefa')
router.register(r'tarefatripulantes', views.TarefaTripulanteView,
                'tarefatripulantes')

urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
