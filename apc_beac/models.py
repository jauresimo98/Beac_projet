from django.db import models

class Tiers(models.Model):
    compte= models.IntegerField(blank=True,null=True)
    centre= models.IntegerField(blank=True,null=True)
    tiers = models.CharField(max_length=254, null=True)
    description = models.CharField(max_length=254, null=True)
    destinataire =  models.CharField(max_length=254, null=True)
    description1  =  models.CharField(max_length=254, null=True)
    description2  =  models.CharField(max_length=254, null=True)
    description3  =  models.CharField(max_length=254, null=True)
    description4  =  models.CharField(max_length=254, null=True)
    description5  =  models.CharField(max_length=254, null=True)
    description6  =  models.CharField(max_length=254, null=True)
    description7  =  models.CharField(max_length=254, null=True)
    etat  =  models.CharField(max_length=254, null=True, default='Actif')

    def __str__(self):
        return self.tiers
    


class Mouvement(models.Model):
    periode = models.CharField(max_length=254, null=True)
    solde = models.CharField(max_length=254, null=True)
    compte= models.IntegerField(blank=True,null=True)
    centre= models.IntegerField(blank=True,null=True)
    tiers = models.CharField(max_length=254, null=True)
    solde_lettre = models.CharField(max_length=254, null=True)
    etat = models.IntegerField(blank=True,null=True)
class Periode(models.Model):
    mois =models.CharField(max_length=254, null=True)
    jour =models.CharField(max_length=254, null=True)
    annee =models.CharField(max_length=254, null=True)


    


# class ReleveCompte(models.Model):
#     numero = models.IntegerField(null=True, blank=True)
#     nomDestinataire = models.CharField(max_length=254, null=True)
#     montant = models.IntegerField(blank=True,null=True)  # Field name made lowercase.
#     date = models.DateTimeField()  # Field name made lowercase.
#     signataire1 = models.CharField(max_length=254, null=True)
#     signataire2 = models.CharField(max_length=254, null=True)
#     signataire3 = models.CharField(max_length=254, null=True)
