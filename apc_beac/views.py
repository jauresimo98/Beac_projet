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
    mvt = Mouvement.objects.all()
    context = {'Mouvement': Mouvement }
    return render(request, 'home.html', context)



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

def template(request):
    return render(request,'template.html')


def recupere_periode (request):
    data=dict()
    
    if request.method=='POST':
        G_jour = request.POST.get('jour')
        G_mois = request.POST.get('mois')
        print(G_jour)
        print(G_mois)
        request.session['G_jour']=request.POST.get('jour')
        request.session['G_mois']=request.POST.get('mois')

    return  render(request,'input.html')
def liste_mvt(request):
    mvt = Mouvement.objects.all()
    return render(request, 'liste_mvt.html', {'mvt': mvt})
def save_mvt_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Tiers.objects.all()
            data['html_book_list'] = render_to_string('tiers/liste_partiel_mvt.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def creer_mvt(request):
    if request.method == 'POST':
        form = MvtForm(request.POST)
    else:
        form = MvtForm()
    return save_mvt_form(request, form, 'tieres/creer_partiel_mvt.html')


def modifier_mvt(request, pk):
    mvt = get_object_or_404(Mouvement, pk=pk)
    if request.method == 'POST':
        form = MvtForm(request.POST, instance=mvt)
    else:
        form = MvtForm(instance=mvt)
    return save_mvt_form(request, form, 'tiers/update_partiel_mvt.html')


def liste_tiers(request):
    tiers = Tiers.objects.all()
    return render(request, 'liste_tiers.html', {'tiers': tiers})



def save_tiers_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Tiers.objects.all()
            data['html_book_list'] = render_to_string('tiers/liste_partiel_tiers.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def creer_tiers(request):
    if request.method == 'POST':
        form = TiersForm(request.POST)
    else:
        form = TiersForm()
    return save_tiers_form(request, form, 'tieres/creer_partiel_tiers.html')


def modifier_tiers(request, pk):
    book = get_object_or_404(Tiers, pk=pk)
    if request.method == 'POST':
        form = TiersForm(request.POST, instance=book)
    else:
        form = TiersForm(instance=book)
    return save_tiers_form(request, form, 'tiers/update_partiel_tiers.html')


def pdf_report_create(request):
    if request.method=='POST':
        num = request.POST.get('numero')
        dest1 = request.POST.get('sign1')
        dest2 = request.POST.get('sign2')
        print(num)
        releve = ReleveCompte.objects.get(numero=num)
        releve.signataire2=dest1
        releve.signataire3=dest2
        releve.save(update_fields=['signataire2','signataire3'])
        nombrelettre=trad(releve.montant)    
    template_path = 'template.html'
    image = Image.objects.all()
    context = {
         'releve':releve,
         'dest1':dest1,
         'dest2':dest2,
         'nombrelettre':nombrelettre,
         'image':image

         }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] =  'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    #return render(request,'template.html', context)

    return response

def afficher_info(request):
    if request.method=='POST':
        compte = request.POST.get('Compte')
        tiers = request.POST.get('Tiers')
        jour = request.POST.get('Jour')
        mois = request.POST.get('Mois')
        annee = request.POST.get('Annee')
        periode = jour + '' +mois + ''+ annee
        mouvement = Mouvement.objects.filter(compte=compte,tiers=tiers,periode = periode)

    return render(request, '')



