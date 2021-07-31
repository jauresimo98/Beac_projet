from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Mouvement,Tiers,Periode
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import FileResponse
import io
from io import BytesIO
from django.contrib import messages
from tablib import Dataset
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views import View
import xhtml2pdf.pisa as pisa
import uuid
from django.core.paginator import Paginator
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def home (request):
    mvt = Mouvement.objects.all()
    context = {'mvt': mvt }
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
    today = datetime.now()
    
    if request.method == 'POST':
        # person_resource = PersonneResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(), format='xlsx')
        # print(imported_data)
        montant = 0
        i = 0
        num = 0
        periode2 =''  
        
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
                #print(solde_int1.replace(',',''))
                #print(compte_int1[12:16])
                num_tiers = str(compte_int)+''+compte_int1[12:16]
                #print(num_tiers)
                num_tiers1 = compte_int
                num_tiers2 = compte_int1[12:16]
                periode = Periode.objects.all()
                for p in periode:
                    #print(p.jour)
                    periode2 = p.jour +' '+ p.mois+' '+str(today.year)

               # periode2 = periode.jour +''+ periode.mois 
                print(periode2)
    


                mouvement= Mouvement(
                    solde = solde,
                    compte = num_tiers1,
                    tiers = num_tiers2,
                    centre = 50,
                    periode = periode2

                )
                mouvement.save()
                Periode.objects.all().delete()

               

    return render(request, 'input.html')




# def simple_upload(request):
    
#     solde_int = ''
#     solde_int1 = ''
#     solde = 0
#     code_compte= ''
#     periode = ' '
#     num_tiers1=0
#     num_tiers2=''
#     num_tiers=''
#     today = datetime.now()
    
#     if request.method == 'POST':
#         # person_resource = PersonneResource()
#         dataset = Dataset()
#         new_persons = request.FILES['myfile']

#         imported_data = dataset.load(new_persons.read(), format='xlsx')
#         # print(imported_data)
#         montant = 0
#         i = 0
#         num = 0
#         periode2 =''
        
#         num_compte = ''
#         compte_int = ' '
#         compte_int1 = ' '

#         for data in imported_data:
#             print(data[10])
#             tiers = Tiers(
#                 centre = data[0],
#                 compte = data[1],
#                 tiers  = data[2],
#                 destinataire = data[3],
#                 description1 = data[4],
#                 description2 = data[5],
#                 description3 = data[6],
#                 description4 = data[7],
#                 description5 = data[8],
#                 description6 = data[9],
#                 description7 = data[10]
#             )

#             tiers.save()
          


#                 # mouvement= Mouvement(
#                 #     solde = solde,
#                 #     compte = num_tiers1,
#                 #     tiers = num_tiers2,
#                 #     centre = 50,
#                 #     periode = periode2

#                 # )
#                 # mouvement.save()
#                 # Periode.objects.all().delete()

               

#     return render(request, 'input.html')


def periode(request):
    return render(request,'periode.html')

def template(request):
    return render(request,'template.html')


def recupere_periode (request):
    data=dict()
    print('recuperation')
    if request.method=='POST':
        G_jour = request.POST.get('jour')
        G_mois = request.POST.get('mois')
        periode1 = Periode(
            mois =  G_mois,
            jour  = G_jour
            
        )

        periode1.save()
        
        #redirect('recupere_periode')
       

    return redirect('input')
def liste_mvt(request):
    mvt = Mouvement.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(mvt, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    return render(request, 'liste_mvt.html', {'users': users,'periode':periode})
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
    sol = 'p' 
    if request.method=='POST':
        compte = request.POST.get('compte')
        tiers = request.POST.get('tiers')
        jour = request.POST.get('jour')
        mois = request.POST.get('mois')
        annee = request.POST.get('annee')
        periode1 = jour +' '+mois+ ' '+ annee
        mouvement = Mouvement.objects.filter(compte=int(compte), tiers=tiers, periode=periode1)
        for mouv in mouvement:
            tiers_mvt=mouv.tiers
            compte_mvt=mouv.compte
            periode_mvt =mouv.periode
            centre_mvt = mouv.centre
            solde_mvt = mouv.solde
            print(type(solde_mvt ))
            solde_teste = int(solde_mvt)
            if solde_teste<0:
                sol ='n'
            nombrelettre=trad(int(solde_mvt))
            
        tiers_table = Tiers.objects.filter(compte=int(compte), tiers=tiers)
        for t in tiers_table:
            dest  = t.destinataire
            desc1 = t.description1
            desc2 = t.description2
            desc3 = t.description3
            desc4 = t.description4
            desc5 = t.description5
            desc6 = t.description6
            desc7 = t.description7 
                             
    template_path = 'template.html'
    context = {
         'dest':dest,
         'desc1':desc1,
         'desc2':desc2,
         'desc3':desc3,
         'desc4':desc4,
         'desc5':desc5,
         'desc6':desc6,
         'desc7':desc7,
         'nombrelettre' : nombrelettre,
         'centre_mvt':centre_mvt,
         'compte_mvt':compte_mvt,
         'tiers_mvt':tiers_mvt,
         'periode_mvt': periode_mvt,
         'solde_mvt':solde_mvt,
         'sol':sol   }
    
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

def pdf_report_create1(request):
    if request.method=='POST':
        compte = request.POST.get('compte')
        tiers = request.POST.get('tiers')
        jour = request.POST.get('jour')
        mois = request.POST.get('mois')
        annee = request.POST.get('annee')
        periode = jour +' '+mois+ ' '+ annee
        mouvement = Mouvement.objects.filter(compte=compte, tiers=tiers, periode=periode)
        print(num)
        #releve = ReleveCompte.objects.get(numero=num)
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


def liste_user(request):
    user_list = Users.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'liste_user.html', { 'users': users })


def tradd(num):
    global t1,t2
    ch=''
    if num==0 :
        ch=''
    elif num<20:
        ch=t1[num]
    elif num>=20:
        if (num>=70 and num<=79)or(num>=90):
            z=int(num/10)-1
        else:
            z=int(num/10)
        ch=t2[z]
        num=num-z*10
        if (num==1 or num==11) and z<8:
            ch=ch+' et'
        if num>0:
            ch=ch+' '+tradd(num)
        else:
            ch=ch+tradd(num)
    return ch


def tradn(num):
    global t1,t2
    ch=''
    flagcent=False
    if num>=1000000000:
        z=int(num/1000000000)
        ch=ch+tradn(z)+' milliard'
        if z>1:
            ch=ch+'s'
        num=num-z*1000000000
    if num>=1000000:
        z=int(num/1000000)
        ch=ch+tradn(z)+' million'
        if z>1:
            ch=ch+'s'
        num=num-z*1000000
    if num>=1000:
        if num>=100000:
            z=int(num/100000)
            if z>1:
                ch=ch+' '+tradd(z)
            ch=ch+' cent'
            flagcent=True
            num=num-z*100000
            if int(num/1000)==0 and z>1:
                ch=ch+'s'
        if num>=1000:
            z=int(num/1000)
            if (z==1 and flagcent) or z>1:
                ch=ch+' '+tradd(z)
            num=num-z*1000
        ch=ch+' mille'
    if num>=100:
        z=int(num/100)
        if z>1:
            ch=ch+' '+tradd(z)
        ch=ch+" cent"
        num=num-z*100
        if num==0 and z>1:
           ch=ch+'s'
    if num>0:
        ch=ch+" "+tradd(num)
    return ch


def trad(nb, unite=" ", decim="centime"):
    global t1,t2
    nb=round(nb,2)
    t1=["","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf"]
    t2=["","dix","vingt","trente","quarante","cinquante","soixante","septante","quatre-vingt","nonante"]
    z1=int(nb)
    z3=(nb-z1)*100
    z2=int(round(z3,0))
    if z1==0:
        ch="zéro"
    else:
        ch=tradn(abs(z1))
    if z1>1 or z1<-1:
        if unite!='':
            ch=ch+" "+unite+'s'
    else:
        ch=ch+" "+unite
    if z2>0:
        ch=ch+tradn(z2)
        if z2>1 or z2<-1:
            if decim!='':
                ch=ch+" "+decim+'s'
        else:
            ch=ch+" "+decim
    if nb<0:
        ch="moins "+ch
    return ch
