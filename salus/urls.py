from django.urls import path

from . import views

from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro_usuario', views.usuario, name='usuarios',),
    path('main', views.main, name='mainClean'),
    path('main', views.main, name='main'),
    path('cadastro_residencia', views.residencia, name='cadastro_residencia'),
    path('cadastro_visita', views.visita, name='cadastro_visita'),
    path('prancheta_visita/<int:id_visita>', views.prancheta, name='prancheta_visita'),
	path('listar_usuarios', views.listar_usuarios, name='listar_usuarios'),
    path('listar_rota', views.listar_rota, name='listar_rota'),
	path('apagar/<int:id>', views.apagar, name='apagar'),
	path('editar/<str:usuario>', views.editar, name='editar'),
	path('justificar_visita', views.justificar_visita, name='justificar_visita'),
    path('ajax/<str:estado_id>/cidades', views.ajax_cidades, name='ajax_cidades'),
    path('ajax/<int:cidade_id>/bairros', views.ajax_bairros, name='ajax_bairros'),
    path('ajax/<int:bairro_id>/ruas', views.ajax_ruas, name='ajax_ruas'),
    path('ajax/<int:rua_id>/casas', views.ajax_casas, name='ajax_casas'),
    #path('rota', views. ,name='rota'),
    path('graficos/<str:cidade>', views.grafico, name='graficos'),
    path('graficos/<str:cidade>/<int:bairro_id>', views.graficoBairro, name='graficoBairro'),
     path('inspecionar_trabalho/<int:id>', views.inspecionar_trabalho, name='inspecionar_trabalho'),
] 
