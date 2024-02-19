from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", views.login, name="login"),
    path("inicio/", views.inicio, name="inicio"),
    path("logout/", views.logout, name="logout"),
    path("categorias/", views.categorias, name="categorias"),
    path("categorias_crear/", views.categorias_crear, name="categorias_crear"),
    path("categorias_guardar/", views.categorias_guardar, name="categorias_guardar"),
    path("categorias_editar/<int:id_categoria>/", views.categorias_editar, name="categorias_editar"),
    path("categorias_eliminar/<int:id_categoria>/", views.categorias_eliminar, name="categorias_eliminar"),
    path("servicios/", views.servicios, name="servicios"),
    path("servicios_crear/", views.servicios_crear, name="servicios_crear"),
    path("servicios_guardar/", views.servicios_guardar, name="servicios_guardar"),
    path("servicios_editar/<int:id_servicio>/", views.servicios_editar, name="servicios_editar"),
    path("servicios_eliminar/<int:id_servicio>/", views.servicios_eliminar, name="servicios_eliminar"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("usuarios_crear/", views.usuarios_crear, name="usuarios_crear"),
    path("usuarios_guardar/", views.usuarios_guardar, name="usuarios_guardar"),
    path("usuarios_editar/<int:id_usuario>/", views.usuarios_editar, name="usuarios_editar"),
    path("usuarios_eliminar/<int:id_usuario>/", views.usuarios_eliminar, name="usuarios_eliminar"),
]
