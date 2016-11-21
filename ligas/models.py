from django.db import models

class Liga(models.Model):
    """ Categorias para registrar ligas """

    name = models.CharField(max_length=50)
    pais = models.CharField(max_length=50,default='/')
    numero = models.CharField(max_length=2,default='20')

    def __str__(self):
        return self.name


class Equipo(models.Model):
    """ Equipos de la liga """

    league = models.ForeignKey(Liga, null=True, blank=True)
    nombre = models.CharField(max_length=50, default=' ')
    color = models.CharField(max_length=50, default=' ')
    capitan = models.CharField(max_length=50, default=' ')
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre
