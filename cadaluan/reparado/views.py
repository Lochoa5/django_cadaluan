from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Q
from .forms import *


def index(request):
    logueo = request.session.get("logueo", False)

    if logueo:
        return redirect("inicio")  # direcciona a la vista llamada inicio
    else:
        return render(request, "reparado/layouts/nuevo_login.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            q = Usuario.objects.get(username=username, password=password)
            messages.success(request, f"Bienvenido {q.nombre}")

            # Crear la sesión......
            request.session["logueo"] = {
                "id": q.id,
                "nombre": q.nombre,
                "rol": q.rol
            }

            return redirect("inicio")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña no válidos...")
            return redirect("index")
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect("index")
    else:
        messages.warning(request, "No se enviaron datos...")
        return redirect("index")


def inicio(request):
    logueo = request.session.get("logueo", False)

    if logueo:
        return render(request, "reparado/home/index.html")
    else:
        return redirect("index")


def logout(request):
    logueo = request.session.get("logueo", False)
    if logueo:
        del request.session["logueo"]
        return redirect("index")
    else:
        messages.info(request, "No se pudo cerrar sesión, intente de nuevo")
        return redirect("inicio")


def categorias(request):
    q = Categoria.objects.all()
    context = {"data": q}
    return render(request, "reparado/categorias/categorias_listar.html", context)


def categorias_crear(request):
    logueo = request.session.get("logueo", False)

    if logueo:
        return render(request, "reparado/categorias/categorias_crear.html")
    else:
        return redirect("index")


def categorias_guardar(request):
    if request.method == "POST":
        nombre_cat = request.POST.get("nombre_cat")
        desc = request.POST.get("desc")
        try:
            q = Categoria(nombre_cat=nombre_cat, desc=desc)
            q.save()
            messages.success(request, "Categoría guardada exitosamente.")
        except Exception as e:
            messages.error(request, f"Error: {e}")
        return redirect("categorias")
    else:
        messages.warning(request, "No se enviaron datos.")
        return redirect("categorias_crear")


def categorias_editar(request, id_categoria):

    categoria = get_object_or_404(Categoria, id=id_categoria)

    if request.method == 'GET':
        # Renderiza el formulario con los datos actuales
        print("Entro oooo")
        return render(request, 'reparado/categorias/categoria_editar_modal.html', {'categoria': categoria})

    elif request.method == 'POST':
        # Procesa el formulario y actualiza la base de datos
        categoria.nombre_cat = request.POST.get('nombre_cat')
        categoria.desc = request.POST.get('desc')
        categoria.save()
        messages.success(request, 'Datos actualizados con éxito!!!')
        return redirect("categorias")


def categorias_eliminar(request):
    pass


def categorias_actualizar(request):
    pass


def servicios(request):
    q = Servicio.objects.all()
    context = {"data": q}
    return render(request, "reparado/servicios/servicios_listar.html", context)


def servicios_crear(request):
    pass


def servicios_guardar(request):
    pass


def servicios_editar(request):
    pass


def servicios_eliminar(request):
    pass


def usuarios(request):
    q = Usuario.objects.all()
    context = {"data": q}
    return render(request, "reparado/usuarios/usuarios_listar.html", context)


def usuarios_crear(request):
    pass


def usuarios_guardar(request):
    pass


def usuarios_editar(request):
    pass


def usuarios_eliminar(request):
    pass


# Vistas para API

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class SolicitudServicioViewSet(viewsets.ModelViewSet):
    queryset = SolicitudServicio.objects.all()
    serializer_class = SolicitudServicioSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


class Metodo_PagoViewSet(viewsets.ModelViewSet):
    queryset = Metodo_Pago.objects.all()
    serializer_class = Metodo_PagoSerializer


class FacturaPagoViewSet(viewsets.ModelViewSet):
    queryset = FacturaPago.objects.all()
    serializer_class = FacturaPagoSerializer
