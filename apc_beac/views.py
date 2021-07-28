from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponse
from .models import Mouvement,Tiers
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import FileResponse
import io
from io import BytesIO
from django.contrib import messages
from tablib import Dataset
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views import View
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.decorators import login_required

# from reste_framework.authtoken.models import Token

# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

# -*- coding: cp1252 -*-

"""
Traduction d'un nombre en texte.
Réalisation : Michel Claveau    http://mclaveau.com

SVP, n'enlevez pas mon adresse/URL ; merci d'avance

Usage : voir les exemples, à la fin du script.

Note : traduction franco-française, avec unités variables, orthographe géré, unités et centièmes.
"""
num = 0
G_mois = ''
G_jour = ''

def home (request):
    return render(request, 'home.html')



def simple_upload(request):
    solde_int = ''
    solde_int1 = ''
    solde = 0
    code_compte= ''
    periode = ' '
    num_tiers1=0
    num_tiers2=''
    num_tiers=''
    
    if request.method == 'POST':
        # person_resource = PersonneResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(), format='xlsx')
        # print(imported_data)
        montant = 0
        i = 0
        num = 0
        
        num_compte = ''
        compte_int = ' '
        compte_int1 = ' '

        for data in imported_data:
            i= i+1
            if i>=12 and i<=159:
                #print(data)
                #print(type(data[3]))
                compte_int = data[1]
                compte_int1 = data[3]
                solde_int = data[8]
                solde_int1 = solde_int[:-4]
                solde = int(solde_int1.replace(',',''))
                #print(compte_int)
                print(solde_int1.replace(',',''))
                #print(compte_int1[12:16])
                num_tiers = str(compte_int)+''+compte_int1[12:16]
                #print(num_tiers)
                num_tiers1 = compte_int
                num_tiers2 = compte_int1[12:16]
                mouvement= Mouvement(
                    solde = solde,
                    compte = num_tiers1,
                    tiers = num_tiers2,
                    centre = 50

                )
                mouvement.save()

               

    return render(request, 'input.html')


def periode(request):
    return render(request,'periode.html')


def recupere_periode (request):
    data=dict()
    
    if request.method=='POST':
        G_jour = request.POST.get('jour')
        G_mois = request.POST.get('mois')
        print(G_jour)
        print(G_mois)

    return  render(request,'input.html')





