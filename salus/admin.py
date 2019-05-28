from django.contrib import admin
from .models import  Residencia, Visita, Prancheta, Bairro, Cidade, Rua, Estado, Rota, Trajeto, Justificar_visita

# Register your models here.
admin.site.register(Residencia)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Rua)
admin.site.register(Visita)
admin.site.register(Estado)
admin.site.register(Rota)
admin.site.register(Trajeto)
admin.site.register(Prancheta)
admin.site.register(Justificar_visita)