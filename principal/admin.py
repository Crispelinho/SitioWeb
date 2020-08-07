from django.contrib import admin

# Register your models here.
from principal.models import Contacto

class ContactosAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","Ncelular","fotogragia","correo")
    search_fields=("nombre","apellido")    
    list_filter=("nombre",)

admin.site.register(Contacto,ContactosAdmin)
