from django.contrib import admin
from .models import Marca, Talla, producto

# Register your models here.

admin.site.register(Marca)
admin.site.register(Talla)
admin.site.register(producto)
