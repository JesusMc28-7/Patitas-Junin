from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

##Prueba de usuarios 

class User(AbstractUser):

    photo = models.ImageField(default="User_default.jpg",upload_to="Users/")
    Cedula = models.CharField(max_length=50, null=True,blank=True)
    Telefono= models .CharField(max_length=50, null=True,blank=True)

    def __str__(self) -> str:
        return self.username
    
##TABLA DE GENEROS    
class Generodb(models.Model):
    gen= models.CharField(max_length=20, verbose_name= "Genero")

    class Meta:
        db_table="Generos"
        verbose_name ="Generos"

    def __str__(self) -> str:
        return self.gen

##TABLA DE ESTELIRIZACION
class Esterilizaciondb(models.Model):
    est= models.CharField(max_length=20, verbose_name= "Genero")

    class Meta:
        db_table="Esterilizacion"
        verbose_name ="Estelirizacion"

    def __str__(self) -> str:
        return self.est
    

## TABLA DE SIZES    
class Tamañodb(models.Model):
    tamaño= models.CharField(max_length=20, verbose_name= "Genero")

    class Meta:
        db_table="Tamaño"
        verbose_name ="Tamaños"

    def __str__(self) -> str:
        return self.tamaño
    

## ESTOS SON LOS VOLUNTARIOS
class Adoptantedb(models.Model):
    ced= models.CharField(max_length=60,primary_key=True,verbose_name="Cedula" )
    name= models.CharField(max_length=30, verbose_name= "Nombre")
    ape= models.CharField(max_length=30, verbose_name= "Apellido")
    tlf= models.CharField(max_length=100,verbose_name= "Telefono")
    correo= models.TextField(max_length=100, verbose_name= "Correo")
    photo = models.ImageField(default="Adoptante_default.png",upload_to="Adoptante/")
    

    class Meta:
        db_table="Voluntarios"
        verbose_name ="Voluntario"
        verbose_name_plural= "Voluntarios"

    def __str__(self) -> str:
        return self.ced


##ESTOS SON LOS PERROS
class Perrosdb(models.Model):
    nom= models.CharField(max_length=40, verbose_name= "Nombre")
    edad= models.IntegerField(verbose_name= "Edad")
    desc= models.TextField(max_length=500, verbose_name= "Descripcion")
    raza= models.CharField(max_length=30, verbose_name= "Raza")
    fk_est=  models.ForeignKey(Esterilizaciondb, on_delete=models.CASCADE,verbose_name= "Estelirizacion")
    fk_tam=  models.ForeignKey(Tamañodb, on_delete=models.CASCADE, verbose_name= "Tamaño")
    fk_gen=  models.ForeignKey(Generodb, on_delete= models.CASCADE, verbose_name= "Genero")
    photo = models.ImageField(default="Perro_default.jpg",upload_to="Perros/")

    class Meta:
        db_table="Perros"
        verbose_name ="Perro"
        verbose_name_plural= "Perros"

    def __str__(self) -> str:
        return self.nom