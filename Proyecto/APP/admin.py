from django.contrib import admin
from .models import *
# Register your models here.

##Vista de usuarios
admin.site.register(User)

##Vistas de Perro
class Perrosadmin(admin.ModelAdmin):
    fields=["id","nom","edad","desc","raza","fk_est","fk_tam","fk_gen","photo"]
    list_display= ["id","nom","edad","fk_est","fk_tam","fk_gen"]

admin.site.register(Perrosdb,Perrosadmin)

##Vista de las vacunas de perro
class Vacunas_perroadmin(admin.ModelAdmin):
    fields=["fk_id","vac1","vac2","vac3"]
    list_display= ["fk_id","vac1","vac2","vac3"]
    
admin.site.register(vacunas_perrodb,Vacunas_perroadmin)

##Vista de adoptante
class adoptanteadmin(admin.ModelAdmin):
    fields=["ced","name","ape","tlf","correo","photo",]
    list_display= ["ced","name","ape"]
    

admin.site.register(Adoptantedb,adoptanteadmin)

##Vista de Gato 
class Gatossadmin(admin.ModelAdmin):
    fields=["id","nom","edad","desc","raza","fk_est","fk_gen","photo"]
    list_display= ["id","nom","edad","fk_est","fk_gen"]
    

admin.site.register(Gatodb,Gatossadmin)

##Vista de las vacunas de gatos
class Vacunas_Gatoadmin(admin.ModelAdmin):
    fields=["fk_id","vac1","vac2","vac3"]
    list_display= ["fk_id","vac1","vac2","vac3"]
    
admin.site.register(vacunas_gatodb,Vacunas_Gatoadmin)

