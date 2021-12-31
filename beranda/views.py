import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .models import CovidData
from .forms import DataCovidForm
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect, HttpResponse


def index(request):
    CovidDatas = CovidData.objects.all()
    response = {'CovidDatas': CovidDatas}
    return render(request, 'beranda.html', response)

def Covid(request):
    CovidDatas = CovidData.objects.all()
    response = {'CovidDatas': CovidDatas}
    return render(request, 'tabel_edit.html', response)

def get_covid_data(request, id):
    CovidDatas = CovidData.objects.get(id=id)
    response = {'CovidDatas': CovidDatas}
    return render(request, 'beranda_forms.html', response)

@login_required(login_url='/admin/login/')
def add_covid_data(request):
    CovidDatas = CovidData.objects.all()
    response = {'CovidDatas': CovidDatas}

    form = DataCovidForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/beranda/edit-covid-data/')

    response['form']= form
    return render(request, "covid_forms.html", response)

@login_required(login_url='/admin/login/')
def update_covid_data(request, id):
    obj = get_object_or_404(CovidData, id = id)
    form = DataCovidForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/beranda/edit-covid-data/')
 
    response = {'form': form}
    return render(request, "update.html", response)

@login_required(login_url='/admin/login/')
def delete_covid_data(request, id):
    response ={}
 
    obj = get_object_or_404(CovidData, id = id)
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/beranda/edit-covid-data/")
 
    return render(request, "delete.html", response)

def getVaksinData(request):
    total_penduduk = 272229372
    vaccineAtLeast1Dose = 140205046
    fullyVaccinated = 96519346
    get1stDose = vaccineAtLeast1Dose - fullyVaccinated
    notVaccinated = total_penduduk - vaccineAtLeast1Dose

    response = {
        'total_penduduk' : total_penduduk,
        'vaccineAtLeast1Dose' : vaccineAtLeast1Dose,
        'fullyVaccinated' : fullyVaccinated,
        'get1stDose' : get1stDose,
        'notVaccinated' : notVaccinated
        }
    return JsonResponse(response, safe=False)


def jsonAllCovData(request):
    covidDatas = CovidData.objects.all()
    data = serializers.serialize('json', covidDatas)
    return HttpResponse(data, content_type="application/json")
    # return JsonResponse(data, safe=False)

@csrf_exempt
def createCovidData(request):
    body = json.loads(request.body)
    bulan = body["bulan"]
    tahun = body["tahun"]
    penambahanKasusPositif = body["penambahanKasusPositif"]
    positifKumulatif = body["positifKumulatif"]


    data = CovidData(bulan= bulan, tahun= tahun, penambahanKasusPositif= penambahanKasusPositif, positifKumulatif= positifKumulatif,)
        
    data.save()

    return JsonResponse({'message': 'success'}, safe=False)