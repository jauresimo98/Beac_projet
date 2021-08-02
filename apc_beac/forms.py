from django import forms
from .models import Tiers,Mouvement

class TiersForm(forms.ModelForm):
    class Meta:
        model = Tiers
        fields = ['centre', 'compte', 'tiers','destinataire','description' ]
        labels = {'centre':'Centre','compte':'Compte','tiers':'Tiers','destinataire':'Destinataire','description1':'Description'}
        widgets={
            'centre': forms.TextInput(attrs={'class':'form-control'}),
            'compte': forms.TextInput(attrs={'class':'form-control'}),
            'tiers': forms.TextInput(attrs={'class':'form-control'}),
            'Tiers': forms.TextInput(attrs={'class':'form-control'}),
            'destinataire': forms.TextInput(attrs={'class':'form-control'}),
            'description1': forms.TextInput(attrs={'class':'form-control'}),
        }
class MvtForm(forms.ModelForm):
    class Meta:
        model = Mouvement
        fields = ( 'centre', 'compte', 'tiers','periode','solde')
