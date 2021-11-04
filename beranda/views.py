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
        return HttpResponseRedirect('/beranda')

    response['form']= form
    return render(request, "covid_forms.html", response)

@login_required(login_url='/admin/login/')
def update_covid_data(request, id):
    # dictionary for initial data with
    # field names as keys
 
    # fetch the object related to passed id
    obj = get_object_or_404(CovidData, id = id)
 
    # pass the object as instance in form
    form = DataCovidForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    response = {'form': form}
 
    return render(request, "beranda.html", response)

@login_required(login_url='/admin/login/')
def delete_covid_data(request, id):
    # dictionary for initial data with
    # field names as keys
    response ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(CovidData, id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "beranda.html", response)

