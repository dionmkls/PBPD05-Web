from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import CovidData
from .forms import DataCovidForm
from django.http.response import HttpResponseRedirect


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