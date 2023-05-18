from django.contrib import admin

# Register your models here.











class AutorAdmin(admin.ModelAdmin):
    #Lista por donde como se muestra en el django admin
    list_display = ('nombre', 'apellido', 'nacionalidad', 'activo' )
    #filtro por el cual se puede buscar en el django admin
    list_search =( 'nombre', 'apellido' )
    #filtro por el cual se puede filtrar en el django admin
    list_filtet = ('activo', 'nacionalidad')

admin.site.register(Autor, AutorAdmin)
