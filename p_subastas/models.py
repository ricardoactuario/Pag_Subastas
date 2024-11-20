from django.db import models

# Create your models here.

class Oferta(models.Model):
    nombre_completo = models.CharField(max_length=100)
    dui_nit = models.CharField(max_length=25)
    correo = models.EmailField()
    teléfono = models.CharField(max_length=25, null=True, blank=True)
    oferta = models.DecimalField(max_digits=12, decimal_places=2)
    artículo = models.CharField(max_length=50)
    id_vehicular = models.CharField(max_length=50)
    kilometraje = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_completo} - {self.vehículo}"