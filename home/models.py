from django.db import models


# Create your models here.


class Chambre(models.Model):
    nom = models.CharField(max_length=20)
    prix = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    disponibilité = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
class Catalogue(models.Model):
    image = models.ImageField(upload_to='pics')

