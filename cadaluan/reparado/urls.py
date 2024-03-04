from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from . import views

router = DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'servicio', views.ServicioViewSet)
router.register(r'solicitud', views.SolicitudViewSet)
router.register(r'solicitud_servicio', views.SolicitudServicioViewSet)
router.register(r'comentario', views.ComentarioViewSet)
router.register(r'auditoria', views.AuditoriaViewSet)
router.register(r'factura', views.FacturaViewSet)
router.register(r'metodo_pago', views.Metodo_PagoViewSet)
router.register(r'factura_pago', views.FacturaPagoViewSet)

urlpatterns = [
    path("api/1.0/", include(router.urls)),
    path('api/1.0/docs/', include_docs_urls(title='Reparado API')),

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
