from django.contrib import admin
from .models import *


# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email']
    search_fields = ['nombre', 'apellido']


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre_cat', 'desc']
    search_fields = ['nombre_cat']  # Para realizar busquedas


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Servicio,)
admin.site.register(Solicitud)
admin.site.register(SolicitudServicio)
admin.site.register(Comentario)
admin.site.register(Auditoria)
admin.site.register(Factura)
admin.site.register(Metodo_Pago)
admin.site.register(FacturaPago)
