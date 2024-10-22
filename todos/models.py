from django.db import models

# Create your models here.
class Atencion_usuarios(models.Model):
    nombre = models.CharField (verbose_name="Nombre " , max_length=50)
    descripcion = models.TextField (verbose_name="Descripcion de usuario")
    precio = models.DecimalField(verbose_name="User id" , max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre