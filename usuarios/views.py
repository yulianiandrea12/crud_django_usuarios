from django.http import JsonResponse
from .models import Usuario

def lista_usuarios(request):
    usuarios = list(Usuario.objects.values())
    return JsonResponse(usuarios, safe=False)

def detalle_usuario(request, codigo):
    try:
        usuario = Usuario.objects.get(codigo=codigo)
        return JsonResponse({
            "codigo": usuario.codigo,
            "nombre": usuario.nombre
        })
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)
