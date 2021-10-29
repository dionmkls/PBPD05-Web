from django.shortcuts import render, redirect
from .models import VaksinJakarta, VaksinBogor, VaksinDepok, VaksinTangerang, VaksinBekasi
from .forms import FormJakarta, FormBogor, FormDepok, FormTangerang, FormBekasi
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def index(request):
    vaksinsJak = VaksinJakarta.objects.all().values()
    vaksinsBog = VaksinBogor.objects.all().values()
    vaksinsDep = VaksinDepok.objects.all().values()
    vaksinsTag = VaksinTangerang.objects.all().values()
    vaksinsBek = VaksinBekasi.objects.all().values()
    response = {
        'vaksinsJak': vaksinsJak,
        'vaksinsBog': vaksinsBog,
        'vaksinsDep': vaksinsDep,
        'vaksinsTag': vaksinsTag,
        'vaksinsBek': vaksinsBek,
    }
    if request.user.is_authenticated:
        return render(request, 'index_vaksin2.html', response)
    else:
        return render(request, 'index_vaksin.html', response)









def index2(request): #nampilin data pake ajax
    # vaksinsJak = serializers.serialize('json', VaksinJakarta.objects.all())
    # vaksinsBog = serializers.serialize('json', VaksinBogor.objects.all())
    # vaksinsDep = serializers.serialize('json', VaksinDepok.objects.all())
    # vaksinsTag = serializers.serialize('json', VaksinTangerang.objects.all())
    # vaksinsBek = serializers.serialize('json', VaksinBekasi.objects.all())
    # vaksinsJak = VaksinJakarta.objects.all()
    # vaksinsBog = VaksinBogor.objects.all()
    # vaksinsDep = VaksinDepok.objects.all()
    # vaksinsTag = VaksinTangerang.objects.all()
    # vaksinsBek = VaksinBekasi.objects.all()

    # hapus data

    vaksinsJak = VaksinJakarta.objects.all().values()
    vaksinsBog = VaksinBogor.objects.all().values()
    vaksinsDep = VaksinDepok.objects.all().values()
    vaksinsTag = VaksinTangerang.objects.all().values()
    vaksinsBek = VaksinBekasi.objects.all().values()

    # ubah queryset ke list python
    
    response = {
        'vaksinsJak': vaksinsJak,
        'vaksinsBog': vaksinsBog,
        'vaksinsDep': vaksinsDep,
        'vaksinsTag': vaksinsTag,
        'vaksinsBek': vaksinsBek,
    }

    # ngapus data, ditampilin ulang
    return render(request, 'index_vaksin3.html', JsonResponse(response))













    
@login_required(login_url='/admin/login/')
def add_jakarta(request):
    form = FormJakarta()

    if request.method == "POST":
        form = FormJakarta(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {'form': form}
    return render(request, "form_jakarta.html", context)

@login_required(login_url='/admin/login/')
def add_bogor(request):
    form = FormBogor()

    if request.method == "POST":
        form = FormBogor(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {'form': form}
    return render(request, "form_bogor.html", context)

@login_required(login_url='/admin/login/')
def add_depok(request):
    form = FormDepok()

    if request.method == "POST":
        form = FormDepok(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {'form': form}
    return render(request, "form_depok.html", context)

@login_required(login_url='/admin/login/')
def add_tangerang(request):
    form = FormTangerang()

    if request.method == "POST":
        form = FormTangerang(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {'form': form}
    return render(request, "form_tangerang.html", context)

@login_required(login_url='/admin/login/')
def add_bekasi(request):
    form = FormBekasi()

    if request.method == "POST":
        form = FormBekasi(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    context = {'form': form}
    return render(request, "form_bekasi.html", context)
