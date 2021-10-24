from django.shortcuts import render, redirect
from .models import VaksinJakarta, VaksinBogor, VaksinDepok, VaksinTangerang, VaksinBekasi
from .forms import FormJakarta, FormBogor, FormDepok, FormTangerang, FormBekasi
from django.contrib.auth.decorators import login_required

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
    return render(request, 'index_vaksin.html', response)

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
