from django.contrib import admin

from proyectosApp.models import proyecto, tecnologia


# Register your models here.
@admin.register(proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('nombre',)
    filter_horizontal = ('tecnologias',)

@admin.register(tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

