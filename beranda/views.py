from django.shortcuts import get_object_or_404, render
from .models import Information
from .forms import InformationForm
from django.http.response import HttpResponseRedirect


def index(request):
    informations = Information.objects.all()
    response = {'informations': informations}
    return render(request, 'beranda.html', response)

def get_information(request, id):
    informations = Information.objects.get(id=id)
    response = {'informations': informations}
    return render(request, 'beranda.html', response)

def add_information(request):
    informations = Information.objects.all()
    response = {'informations': informations}

    form = InformationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/beranda')

    response['form']= form
    return render(request, "beranda.html", response)


def update_information(request, id):
    # dictionary for initial data with
    # field names as keys
 
    # fetch the object related to passed id
    obj = get_object_or_404(Information, id = id)
 
    # pass the object as instance in form
    form = InformationForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    response = {'form': form}
 
    return render(request, "beranda.html", response)


def delete_information(request, id):
    # dictionary for initial data with
    # field names as keys
    response ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Information, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "beranda.html", response)