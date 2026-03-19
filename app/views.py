from django.shortcuts import render

def pasaporte_amor(request):
    contexto = {
        "novios": "Armando & Jessica",
        "fecha_evento": "11 de octubre de 2026",
        "hora_evento": "18:30 hrs",
        "lugar": "Centro de Eventos Santa Catalina de Chicureo",
        "whatsapp": "+56912345678",
        "lista_regalos": "https://milistadenovios.cl/enviar.php?id=31237"
    }
    return render(request, "pasaporte.html", contexto)

def index(request):
    return render(request, 'app/index.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def acerca_de(request):
    return render(request, 'app/acerca_de.html')





