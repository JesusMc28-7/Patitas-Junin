from django.db import models

# Create your models here.

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
class Voluntariodb(models.Model):
    ced= models.IntegerField(primary_key=True,verbose_name="Cedula" )
    name= models.CharField(max_length=30, verbose_name= "Nombre")
    ape= models.CharField(max_length=30, verbose_name= "Descripcion")
    tlf= models.IntegerField(verbose_name= "Edad")
    correo= models.TextField(max_length=30, verbose_name= "Raza")
    

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
    fk_est=  models.ForeignKey(Esterilizaciondb, on_delete=models.CASCADE)
    fk_tam=  models.ForeignKey(Tamañodb, on_delete=models.CASCADE)
    fk_gen=  models.ForeignKey(Generodb, on_delete= models.CASCADE)

    class Meta:
        db_table="Perros"
        verbose_name ="Perro"
        verbose_name_plural= "Perros"

    def __str__(self) -> str:
        return self.nom