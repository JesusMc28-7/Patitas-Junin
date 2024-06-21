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
        db_table="Adoptantes"
        verbose_name ="Adoptante"
        verbose_name_plural= "Adoptantes"

    def __str__(self) -> str:
        return self.ced


##ESTOS SON LOS PERROS
class Perrosdb(models.Model):
    id= models.CharField(primary_key=True, max_length=50,verbose_name="ID")
    nom= models.CharField(max_length=40, verbose_name= "Nombre")
    edad= models.IntegerField(verbose_name= "Edad")
    desc= models.TextField(max_length=500, verbose_name= "Descripcion")
    raza= models.CharField(max_length=30, verbose_name= "Raza")
    fk_est=  models.ForeignKey(Esterilizaciondb, on_delete=models.CASCADE,verbose_name= "Estelirizacion")
    fk_tam=  models.ForeignKey(Tamañodb, on_delete=models.CASCADE, verbose_name= "Tamaño")
    fk_gen=  models.ForeignKey(Generodb, on_delete= models.CASCADE, verbose_name= "Genero")
    photo = models.ImageField(default="Perro_default.jpg",upload_to="Perros/")

    class Meta:
        db_table="Perro"
        verbose_name ="Perro"
        verbose_name_plural= "Perros"

    def __str__(self) -> str:
        return self.nom
    
 ## VACUNAS PARA PERRO   
class vacunas_perrodb(models.Model):
    fk_id= models.ForeignKey(Perrosdb,verbose_name="ID",on_delete=models.CASCADE)
    vac1= models.CharField (max_length=50, verbose_name="Parvovirus",default= None)
    vac2= models.CharField (max_length=50, verbose_name="Vacuna 2",default= None)
    vac3= models.CharField (max_length=50, verbose_name="Vacuna 3",default= None)
    
    class Meta:
        db_table="Vacunas_Perros"
        verbose_name ="Vacunas_perro"
        verbose_name_plural= "Vacunas_perros"

    
    
##ESTOS SON LOS GATOS
class Gatodb(models.Model):
    id= models.CharField(primary_key=True, max_length=50,verbose_name="ID")
    nom= models.CharField(max_length=40, verbose_name= "Nombre")
    edad= models.IntegerField(verbose_name= "Edad")
    desc= models.TextField(max_length=500, verbose_name= "Descripcion")
    raza= models.CharField(max_length=30, verbose_name= "Raza")
    fk_est=  models.ForeignKey(Esterilizaciondb, on_delete=models.CASCADE,verbose_name= "Estelirizacion")
    fk_gen=  models.ForeignKey(Generodb, on_delete= models.CASCADE, verbose_name= "Genero")
    photo = models.ImageField(default="Gato_default.jpg",upload_to="Gatos/")

    class Meta:
        db_table="Gatos"
        verbose_name ="Gato"
        verbose_name_plural= "Gatos"

    def __str__(self) -> str:
        return self.nom

   ##VACUNAS PARA GATO 
class vacunas_gatodb(models.Model):
    fk_id= models.ForeignKey(Gatodb,verbose_name="ID",on_delete=models.CASCADE)
    vac1= models.CharField (max_length=50, verbose_name="Giardiasis",default= None)
    vac2= models.CharField (max_length=50, verbose_name="Vacuna 2",default= None)
    vac3= models.CharField (max_length=50, verbose_name="Vacuna 3",default= None)

    class Meta:
        db_table="Vacunas Gatos"
        verbose_name ="Vacunas Gato"
        verbose_name_plural= "Vacunas_Gatos"