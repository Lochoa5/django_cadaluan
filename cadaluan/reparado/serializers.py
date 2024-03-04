from .models import *
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'email', 'direccion', 'foto']

        # fields = '__all__'
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # fields = ['id', 'nombre', 'apellido', 'email', 'direccion']
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre_ser', 'desc_ser', 'precio']
        # fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        # fields = ['id', 'nombre', 'apellido', 'email', 'direccion']
        fields = '__all__'

class SolicitudServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudServicio
        fields = ['id_solicitud', 'id_servicio', 'cantidad', 'precio_historico']
        # fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id_solicitud', 'estado', 'comentario']
        # fields = '__all__'

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        # fields = ['id_solicitud', 'estado', 'comentario']
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        # fields = ['id_solicitud', 'estado', 'comentario']
        fields = '__all__'

class Metodo_PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodo_Pago
        # fields = ['id_solicitud', 'estado', 'comentario']
        fields = '__all__'

class FacturaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaPago
        # fields = ['id_solicitud', 'estado', 'comentario']
        fields = '__all__'