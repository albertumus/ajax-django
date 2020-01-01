from django.db import models

# Create your models here.


class Pelicula(models.Model):

    nombre = models.CharField(max_length=300, blank=True, null=True)
    favorita = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.nombre




