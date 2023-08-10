from django.db import models


class Eleve(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    password = models.CharField(max_length=250)

