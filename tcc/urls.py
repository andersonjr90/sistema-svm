from django.contrib import admin
from django.urls import path, include
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
    path('api/', include(router.urls)),
    path('api/login/', views.LoginView.as_view())
]
