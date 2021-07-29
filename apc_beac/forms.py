from django import forms
from .models import Tiers,Mouvement

class TiersForm(forms.ModelForm):
    class Meta:
        model = Tiers
        fields = ('centre', 'compte', 'tiers','destinataires','description' )

class MvtForm(forms.ModelForm):
    class Meta:
        model = Mouvement
        fields = ( 'centre', 'compte', 'tiers','periode','solde')
