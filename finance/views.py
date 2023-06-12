from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bilan, Type
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    types = Type.objects.all()
    bilans = Bilan.objects.filter(owner=request.user)
    paginator = Paginator(bilans, 2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'bilans': bilans,
        'page_obj': page_obj
    }
    return render(request, 'finance/index.html', context)

def add_bilan(request):
    types = Type.objects.all()
    context = {
        'types': types,
        'value': request.POST 
    }
    if request.method == 'GET':
        return render(request, 'finance/add_bilan.html', context)

    if request.method == 'POST':
        actif_immobilisé = request.POST['actif_immobilisé']

        if not actif_immobilisé:
            messages.error(request, 'Actif immobilisé is required')
            return render(request, 'finance/add_bilan.html', context)
        stock = request.POST['stock']
        créances = request.POST['créances']
        trésorerie_actif = request.POST['trésorerie_actif']
        capitaux_propre = request.POST['capitaux_propre']
        dette_de_financement = request.POST['dette_de_financement']
        dette_à_court_terme = request.POST['dette_à_court_terme']
        type = request.POST['type']
        date = request.POST['bilan_date']

        if not stock:
            messages.error(request, 'Stock is required')
            return render(request, 'finance/add_bilan.html', context)
        if not créances:
            messages.error(request, 'Créances is required')
            return render(request, 'finance/add_bilan.html', context)
        if not trésorerie_actif:
            messages.error(request, 'Trésorerie is required')
            return render(request, 'finance/add_bilan.html', context)
        if not capitaux_propre:
            messages.error(request, 'Capitaux propre is required')
            return render(request, 'finance/add_bilan.html', context)
        if not dette_de_financement:
            messages.error(request, 'dette de financement is required')
            return render(request, 'finance/add_bilan.html', context)
        if not dette_à_court_terme:
            messages.error(request, 'Dette à court terme is required')
            return render(request, 'finance/add_bilan.html', context)


        Bilan.objects.create(owner=request.user, actif_immobilisé=actif_immobilisé, stock=stock, créances=créances, trésorerie_actif=trésorerie_actif, capitaux_propre=capitaux_propre, dette_de_financement=dette_de_financement, dette_à_court_terme=dette_à_court_terme, type=type, date=date)

        messages.success(request, 'Bilan saved successffully')

        return redirect('finance')
    

def bilan_edit(request, id):
    bilan = Bilan.objects.get(pk=id)
    types = Type.objects.all()
    context = {
        'bilan' : bilan,
        'values' : bilan,
        'types' : types
    }
    if request.method=='GET':
        return render(request, 'finance/edit-bilan.html', context)
 
    if request.method == 'POST':
        actif_immobilisé = request.POST['actif_immobilisé']

        if not actif_immobilisé:
            messages.error(request, 'Actif immobilisé is required')
            return render(request, 'finance/edit-bilan.html', context)
        stock = request.POST['stock']
        créances = request.POST['créances']
        trésorerie_actif = request.POST['trésorerie_actif']
        capitaux_propre = request.POST['capitaux_propre']
        dette_de_financement = request.POST['dette_de_financement']
        dette_à_court_terme = request.POST['dette_à_court_terme']
        type = request.POST['type']
        date = request.POST['bilan_date']

        if not stock:
            messages.error(request, 'Stock is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not créances:
            messages.error(request, 'Créances is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not trésorerie_actif:
            messages.error(request, 'Trésorerie is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not capitaux_propre:
            messages.error(request, 'Capitaux propre is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not dette_de_financement:
            messages.error(request, 'dette de financement is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not dette_à_court_terme:
            messages.error(request, 'Dette à court terme is required')
            return render(request, 'finance/edit-bilan.html', context)


        bilan.owner = request.user
        bilan.stock = stock
        bilan.créances = créances
        bilan.trésorerie_actif = trésorerie_actif
        bilan.capitaux_propre = capitaux_propre
        bilan.dette_de_financement = dette_de_financement
        bilan.dette_à_court_terme = dette_à_court_terme
        bilan.type = type
        bilan.date = date

        bilan.save()
        messages.success(request, 'Bilan updated  successfully')

        return redirect('finance')

def delete_bilan(request, id):
    bilan = Bilan.objects.get(pk=id)
    bilan.delete()
    messages.success(request, 'Bilan removed')
    return redirect('finance')      