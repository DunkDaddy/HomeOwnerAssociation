from django.db import models

# Create your models here.

class Beboer(models.Model):
    navn = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    tlf = models.BigIntegerField()
    brugernavn = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)

    def __str__(self):
        return self.navn


#class Location(models.Model):
#    lattitude = models.DecimalField(max_digits=8, decimal_places=6)
#    longtitude = models.DecimalField(max_digits=9, decimal_places=6)
    #altitude = models


class Regler(models.Model):
    regel = models.CharField(max_length=255)
    beskrivelse = models.TextField()

    def __str__(self):
        return self.regel


class Andmeldelse(models.Model):
    andmelder_id = models.ForeignKey(Beboer, on_delete=models.CASCADE)
    regel_id = models.ForeignKey(Regler, on_delete=models.CASCADE)
    lattitude = models.DecimalField(max_digits=9, decimal_places=6)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6)

