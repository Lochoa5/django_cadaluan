from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.db.models import Q


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
    pass


def categorias_guardar(request):
    pass


def categorias_editar(request, id_categoria):
    # Obtén la instancia de Categoria por su clave primaria
    c = get_object_or_404(Categoria, pk=id_categoria)

    if request.method == "POST":
        try:
            # Actualiza los campos de la instancia de Categoria con los valores del formulario
            c.nombre_cat = request.POST.get("nombre_cat")
            c.desc = request.POST.get("desc")
            c.save()

            messages.success(request, "Registro actualizado correctamente!!")
        except Exception as e:
            messages.error(request, f"Error: {e}")
    else:
        # Si la solicitud no es un POST, puedes realizar acciones adicionales o simplemente renderizar la plantilla.
        pass

    return redirect("categorias")


def categorias_eliminar(request):
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
