from django.http import HttpResponse

# Cada función creada dentro de este archivo 'views' se le denominará vista

# Primera vista
def saludo(request):
    return HttpResponse("Hola Mundo Django")


# Segunda Vista
def despedida(request):
    return HttpResponse("Hasta Pronto Django")