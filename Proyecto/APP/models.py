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

## TABLA DE ESPECIES GATO/PERRO, pero como puede escalar vamos a dar la opcion de que ingresen la especie de animal    
class Tipodb(models.Model):
    especie= models.CharField(max_length=20, verbose_name= "Especie")

    class Meta:
        db_table="Tipo"
        verbose_name ="Tipos"
        verbose_name_plural= "Tipos"

    def __str__(self) -> str:
        return self.especie
    

## ESTOS SON LOS ADOPTANTES
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


##ESTOS SON LOS ANIMALES/ HAY UN bug QUE EVITA QUE RETORNE UN STR, POR ESO EN SUPER ADMIN EL NOMBRE LO RETORNA COMO Animalesdb object
##Se buguea en la tabla de resguardos
class Animalesdb(models.Model):
    id= models.CharField(primary_key=True, max_length=50,verbose_name="ID")
    nom= models.CharField(max_length=40, verbose_name= "Nombre")
    edad= models.IntegerField(verbose_name= "Edad")
    desc= models.TextField(max_length=500, verbose_name= "Descripcion")
    obs= models.TextField(max_length=500, verbose_name= "Observaciones")
    raza= models.CharField(max_length=30, verbose_name= "Raza")
    fk_est=  models.ForeignKey(Esterilizaciondb, on_delete=models.CASCADE,verbose_name= "Estelirizacion")
    fk_esp= models.ForeignKey(Tipodb, on_delete=models.CASCADE, verbose_name="Especie",default=None)
    fk_tam=  models.ForeignKey(Tamañodb, on_delete=models.CASCADE, verbose_name= "Tamaño")
    fk_gen=  models.ForeignKey(Generodb, on_delete= models.CASCADE, verbose_name= "Genero")
    photo = models.ImageField(default="Animal_default.jpg",upload_to="Animal/")

    class Meta:
        db_table="Animales"
        verbose_name ="Animal"
        verbose_name_plural= "Animales"

    def __str__(self) -> str:
            return self.nom
    
## TABLA DE ASOCIACION DE RESCATISTAS USERS Y ANIMALES EN LA FUNDACION
class Resguardodb(models.Model):
    Cuidador= models.ForeignKey(User, on_delete=models.CASCADE)
    mascota= models.ForeignKey(Animalesdb,on_delete=models.CASCADE)
    
    class Meta:
        db_table="Resguardo"
        verbose_name ="Resguardo"
        ##Si sacan la funcion de self de la clase meta Se cargan todo,asi pueden ver el error
        ## Devuelvanla dentro de la clase meta para que todo vuelva a funcionar
        def __str__(self) -> str:
            return self.mascota
        
##TABLA DE ADOPCIONES
class Adopcionesdb(models.Model):
    id= models.CharField(primary_key=True, max_length=50,verbose_name="Id") 
    Adoptante= models.ForeignKey(Adoptantedb,on_delete=models.CASCADE)
    Animal= models.ForeignKey(Resguardodb,on_delete=models.CASCADE)
    Fecha= models.DateField(verbose_name="Fecha de adopcion")

    class Meta:
        db_table="Adopciones"
        verbose_name ="Adopciones"
        verbose_name_plural= "Adopciones"
        

    def __str__(self) -> str:
            return self.id
    
    ##TABLE DE ANIMALES FALLECIDOS
class Fallecimientodb(models.Model):
    id= models.CharField(primary_key=True, max_length=50,verbose_name="Id") 
    causa_muerte= models.TextField(max_length=100,verbose_name="Causas")
    Animal= models.ForeignKey(Resguardodb,on_delete=models.CASCADE)
    Fecha= models.DateField(verbose_name="Fecha de muerte")

    class Meta:
        db_table="Fallecimientos"
        verbose_name ="Animales_Fallecidos"
        
    def __str__(self) -> str:
        return self.id
    
    ##TABLE DE historial de adopciones
class Historial_Adb(models.Model):
    id= models.CharField(primary_key=True, max_length=50,verbose_name="Id") 
    fk_id= models.ForeignKey(Adopcionesdb,on_delete=models.CASCADE)

    class Meta:
        db_table="Historial_Adopciones"
        verbose_name ="Historial de adopciones"
        
    def __str__(self) -> str:
        return self.id
    
    ##TABLE DE historial de fallecimientos
class Historial_Fdb(models.Model):
    id= models.CharField(primary_key=True, max_length=50,verbose_name="Id") 
    fk_id= models.ForeignKey(Fallecimientodb,on_delete=models.CASCADE)

    class Meta:
        db_table="Historial_Fallecimiento"
        verbose_name ="Historial de Fallecimiento"
        
    def __str__(self) -> str:
        return self.id