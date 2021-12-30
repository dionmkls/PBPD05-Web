from django.http import response
from django.http.response import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import RumahSakit
from .forms import RumahSakitForm

# Create your views here.

def index(request):
    rumah_sakit = RumahSakit.objects.all().values()
    response = {
        'page_title': 'Rumah Sakit',
        'rumah_sakit_ls': rumah_sakit,
    }
    return render(request, 'rumah_sakit_index.html', response)


@login_required(login_url="/admin/login/")
def add_rs(request):
    rumah_sakit = RumahSakitForm(request.POST or None)

    response = {
        'page_title': 'Form Rumah Sakit',
        'rumah_sakit_form': rumah_sakit,
    }

    if request.method == "POST":
        if rumah_sakit.is_valid():
            rumah_sakit.save()
            return redirect('rs_index')

    return render(request, 'rumah_sakit_form.html', response)


# source: GeeksforGeeks
@login_required(login_url="/admin/login/")
def edit_rs(request,id):
    # fetch the object related to passed id
    obj = get_object_or_404(RumahSakit, id = id)

    # dictionary for initial data with
    # field names as keys
    response = {
        'page_title': 'Edit Rumah Sakit',
    }
 
    # pass the object as instance in form
    form = RumahSakitForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('rs_index')
 
    # add form dictionary to context
    response["rumah_sakit_form"] = form
 
    return render(request, "rumah_sakit_edit.html", response)


@login_required(login_url="/admin/login/")
def hapus_rs(request,id):
    # fetch the object related to passed id
    obj = get_object_or_404(RumahSakit, id = id)

    # dictionary for initial data with
    # field names as keys
    response = {
        'page_title': 'Hapus Rumah Sakit',
        'rumah_sakit': obj,
    }
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to rs main page
        return redirect('rs_index')
 
    return render(request, "rumah_sakit_hapus.html", response)


# api

def json_view(request):
    rumah_sakit = RumahSakit.objects.all()
    data = serializers.serialize('json', rumah_sakit)
    return HttpResponse(data, content_type="application/json")

def xml_view(request):
    rumah_sakit = RumahSakit.objects.all()
    data = serializers.serialize('xml', rumah_sakit)
    return HttpResponse(data, content_type="application/xml")
