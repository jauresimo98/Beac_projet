from django.db import models

class Tiers(models.Model):
    compte= models.IntegerField(blank=True,null=True)
    centre= models.IntegerField(blank=True,null=True)
    tiers = models.CharField(max_length=254, null=True)
    destinataire = models.CharField(max_length=254, null=True)
    description = models.CharField(max_length=254, null=True)
    def __str__(self):
        return self.tiers

class Mouvement(models.Model):
    numero = models.ForeignKey(Tiers, null = True, on_delete = models.SET_NULL)
    periode = models.CharField(max_length=254, null=True)
    solde = models.CharField(max_length=254, null=True)
    compte= models.IntegerField(blank=True,null=True)
    centre= models.IntegerField(blank=True,null=True)
    tiers = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.tiers


# class ReleveCompte(models.Model):
#     numero = models.IntegerField(null=True, blank=True)
#     nomDestinataire = models.CharField(max_length=254, null=True)
#     montant = models.IntegerField(blank=True,null=True)  # Field name made lowercase.
#     date = models.DateTimeField()  # Field name made lowercase.
#     signataire1 = models.CharField(max_length=254, null=True)
#     signataire2 = models.CharField(max_length=254, null=True)
#     signataire3 = models.CharField(max_length=254, null=True)


# class Image(models.Model):
#     image = models.ImageField(upload_to='static/images/')

# Create your models here.

# Create your models here.
