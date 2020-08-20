from django.contrib import admin

# Register your models here.
from gestioncontactos.models import Contacto

class ContactosAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","Ncelular","fotografia","correo")
    search_fields=("nombre","apellido")    
    list_filter=("nombre",)

admin.site.register(Contacto,ContactosAdmin)
