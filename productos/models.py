from django.db import models

# Create your models here.

class Marca(models.Model):
    id_marca  = models.AutoField(db_column='idMarca', primary_key=True) 
    marca     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.marca)

class Talla(models.Model):
    id_talla  = models.AutoField(db_column='idTalla', primary_key=True) 
    talla     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.talla)


class producto(models.Model):
    id_prod          = models.CharField(primary_key=True, max_length=10)
    nombre_prod      = models.CharField(max_length=20)
    id_marca         = models.ForeignKey('Marca',on_delete=models.CASCADE, db_column='idMarca')  
    id_talla         = models.ForeignKey('Talla',on_delete=models.CASCADE, db_column='idTalla')
    color            = models.CharField(max_length=20)  
    precio           = models.IntegerField()
    imagen           = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return str(self.nombre_prod)+" "+str(self.color)+" "+str(self.precio)