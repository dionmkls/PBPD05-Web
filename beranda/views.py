from django.shortcuts import get_object_or_404, render
from .models import CovidData, VaksinData
from .forms import DataCovidForm, DataVaksinForm
from django.http.response import HttpResponseRedirect


def index(request):
    CovidDatas = CovidData.objects.all()
    response = {'CovidDatas': CovidDatas}
    return render(request, 'beranda.html', response)

def Covid(request):
    CovidDatas = CovidData.objects.all()
    response = {'CovidDatas': CovidDatas}
    return render(request, 'beranda.html', response)

def get_covid_data(request, id):
    CovidDatas = CovidData.objects.get(id=id)
    response = {'CovidDatas': CovidDatas}
    return render(request, 'beranda_forms.html', response)

def add_covid_data(request):
    CovidDatas = CovidData.objects.all()
    response = {'CovidDatas': CovidDatas}

    form = DataCovidForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/beranda')

    response['form']= form
    return render(request, "covid_forms.html", response)

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




# data vaksin
def Vaksin(request):
    VaksinDatas = VaksinData.objects.all()
    response = {'VaksinDatas': VaksinDatas}
    return render(request, 'beranda.html', response)

def get_vaksin_data(request, id):
    VaksinDatas = VaksinData.objects.get(id=id)
    response = {'VaksinDatas': VaksinDatas}
    return render(request, 'vaksin_forms.html', response)

def add_vaksin_data(request):
    VaksinDatas = VaksinData.objects.all()
    response = {'VaksinDatas': VaksinDatas}

    form = DataVaksinForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/beranda')

    response['form']= form
    return render(request, "vaksin_forms.html", response)

def update_vaksin_data(request, id):
    # dictionary for initial data with
    # field names as keys
 
    # fetch the object related to passed id
    obj = get_object_or_404(VaksinData, id = id)
 
    # pass the object as instance in form
    form = DataVaksinForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    response = {'form': form}
 
    return render(request, "beranda.html", response)

def delete_vaksin_data(request, id):
    # dictionary for initial data with
    # field names as keys
    response ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(VaksinData, id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "beranda.html", response)