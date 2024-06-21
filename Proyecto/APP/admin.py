from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)

class Perrosadmin(admin.ModelAdmin):
    fields=["nom","edad","desc","raza","fk_est","fk_tam","fk_gen","photo"]
    list_display= ["nom","edad","fk_est","fk_tam","fk_gen"]

admin.site.register(Perrosdb,Perrosadmin)


class adoptanteadmin(admin.ModelAdmin):
    fields=["ced","name","ape","tlf","correo","photo",]
    list_display= ["ced","name","ape"]

admin.site.register(Adoptantedb,adoptanteadmin)