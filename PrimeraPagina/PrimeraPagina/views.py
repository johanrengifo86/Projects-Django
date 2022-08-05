from django.http import HttpResponse

# Se crea este archivo para las vistas que tendrá el proyecto web

# Cada función creada dentro de este archivo 'views' se le denominará vista

# Primera vista
def saludo(request):
    return HttpResponse("Hola Mundo Django")


# Segunda Vista
def despedida(request):
    return HttpResponse("Hasta Pronto Django")