from django.contrib import admin
from .models import *
# Register your models here.

##Vista de usuarios
admin.site.register(User)

##Vista de adoptante
class adoptanteadmin(admin.ModelAdmin):
    fields=["ced","name","ape","tlf","correo","photo",]
    list_display= ["ced","name","ape"]
    

admin.site.register(Adoptantedb,adoptanteadmin)

##Vista de las especies
class Tipodmin(admin.ModelAdmin):
    fields=["especie"]
    list_display= ["especie"]
    
admin.site.register(Tipodb,Tipodmin)

class Generosadmin(admin.ModelAdmin):
    fields=["gen"]
    list_display= ["gen"]

admin.site.register(Generodb,Generosadmin)

class Tamañosadmin(admin.ModelAdmin):
    fields=["tamaño"]
    list_display= ["tamaño"]

admin.site.register(Tamañodb,Tamañosadmin)

class Estelirizacionadmin(admin.ModelAdmin):
    fields=["est"]
    list_display= ["est"]

admin.site.register(Esterilizaciondb,Estelirizacionadmin)




##Vistas de Animales
class Animalesadmin(admin.ModelAdmin):
    fields=["id","nom","edad","desc","obs","raza","fk_est","fk_esp","fk_tam","fk_gen","photo"]
    list_display= ["id","nom","edad","fk_esp","fk_est","fk_tam","fk_gen"]

admin.site.register(Animalesdb,Animalesadmin)

##Vista de Resguardo 
class Resguardoadmin(admin.ModelAdmin):
    fields=["Cuidador","mascota"]
    list_display= ["Cuidador","mascota"]
    

admin.site.register(Resguardodb,Resguardoadmin)

##Vista de Adopciones 
class Adopcionesadmin(admin.ModelAdmin):
    fields=["id","Adoptante","Animal","Fecha"]
    list_display= ["id","Adoptante","Animal","Fecha"]
    
admin.site.register(Adopcionesdb,Adopcionesadmin)

##Vista de Adopciones 
class Fallecimientosadmin(admin.ModelAdmin):
    fields=["id","causa_muerte","Animal","Fecha"]
    list_display= ["id","Animal","Fecha"]
    
admin.site.register(Fallecimientodb,Fallecimientosadmin)


##Vista de Adopciones 
class Historial_A_admin(admin.ModelAdmin):
    fields=["id","fk_id"]
    list_display= ["id","fk_id"]
    
admin.site.register(Historial_Adb,Historial_A_admin)

class Historial_F_admin(admin.ModelAdmin):
    fields=["id","fk_id"]
    list_display= ["id","fk_id"]
    
admin.site.register(Historial_Fdb,Historial_F_admin)
