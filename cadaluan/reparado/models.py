from django.db import models


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=254)
    apellido = models.CharField(max_length=254)
    username = models.CharField(max_length=100, unique=True, default='user')
    email = models.EmailField()
    direccion = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    foto = models.ImageField(upload_to="usuarios/", default="usuarios/default.png")

    ROLES = (
        ("ADMIN", "Administrador"),
        ("SECRE", "Secretaria"),
        ("VENDE", "Vendedor"),
        ("USUAR", "Usuario"),
    )
    rol = models.CharField(max_length=5, choices=ROLES, default="USUAR", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    nombre_cat = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return f"{self.nombre_cat}"


class Servicio(models.Model):
    nombre_ser = models.CharField(max_length=200)
    desc_ser = models.TextField()
    precio = models.IntegerField()
    id_categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="productos/", default="productos/default.png")

    def __str__(self):
        return f"{self.nombre_ser}"


class Solicitud(models.Model):
    fecha_hora = models.DateTimeField()
    estado_cita = models.CharField(max_length=200)
    zona = models.CharField(max_length=200)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)


class SolicitudServicio(models.Model):
    id_solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_historico = models.IntegerField()
    foto = models.ImageField(upload_to="fotos_productos/", default="fotos_productos/default.png")


class Comentario(models.Model):
    id_solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    estado = models.CharField(max_length=200)
    comentario = models.CharField(max_length=254)
    estrellas = models.IntegerField()

    def __str__(self):
        return f"Comentario para Solicitud {self.id_solicitud}"


class Auditoria(models.Model):
    fecha_modificacion = models.DateTimeField(auto_now=True)


class Factura(models.Model):
    id_solicitud = models.ForeignKey(Solicitud, on_delete=models.DO_NOTHING)
    fecha_emision = models.DateField()
    total = models.IntegerField()


class Metodo_Pago(models.Model):
    nombre_Metodo = models.CharField(max_length=200)
    desc_metodo = models.TextField()


class FacturaPago(models.Model):
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    id_pago = models.ForeignKey(Metodo_Pago, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto = models.IntegerField()
