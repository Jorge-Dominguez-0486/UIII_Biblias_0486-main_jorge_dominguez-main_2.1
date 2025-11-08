from django.contrib import admin
# Modifica esta línea para importar Pedido
from .models import ClienteGlobal, Pedido

admin.site.register(ClienteGlobal)
# Agrega esta línea
admin.site.register(Pedido)