from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola! Esta es la página principal del backend, escribe /api/ al final de la URL para mejor visualización de la app y /authors/ para conocer los desarrolladores.")

from django.http import JsonResponse

def authors(request):
    data = {
        "integrantes": [
            {"nombre": "Ana Pérez", "código": "202412345"},
            {"nombre": "Luis Gómez", "código": "202498765"},
            # Agrega más integrantes aquí si es necesario
        ]
    }
    return JsonResponse(data)


urlpatterns = [
    path('', home), 
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  
    path('authors/', authors),  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
