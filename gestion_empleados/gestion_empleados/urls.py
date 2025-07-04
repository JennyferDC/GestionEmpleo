from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido al sistema de gestión de empleados.")

urlpatterns = [
    path("", home), 
    path('admin/', admin.site.urls),
    path('api/', include('empleados_app.api.urls')),  # <--- Incluye la API aquí
]