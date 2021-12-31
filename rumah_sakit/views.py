from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

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

# flutter

def flutter(request):
    if request.GET['from'] != "flutter": # dari flutter
        return JsonResponse({
            'message': 'Denied',
        }, safe=False)

    if request.GET['to'] == "delete":
        return hapus_rs_f(request)
    elif request.GET['to'] == "edit":
        return get_rs_data(request)
    else:
        rumah_sakit = RumahSakit.objects.all()
        data = serializers.serialize('json', rumah_sakit)
        return JsonResponse(data, safe=False)

def hapus_rs_f(request):
    idRS = request.GET['id']

    obj = get_object_or_404(RumahSakit, id = idRS)

    nama = obj.nama
    print(nama + " berhasil di hapus")
    # hapus object
    obj.delete()

    return JsonResponse({
        'nama': nama,
    }, safe=False)

def get_rs_data(request):
    idRS = request.GET['id']

    obj = get_object_or_404(RumahSakit, id = idRS)
    data = serializers.serialize('json', obj)

    return JsonResponse(data, safe=False)

@csrf_exempt
def add_flutter(request):
    body = json.loads(request.body)

    nama = body["nama"]
    lokasi = body["lokasi"]
    alamat = body["alamat"]
    url_gmaps = body["url_gmaps"]
    no_telp = body["no_telp"]
    tersedia = body["tersedia"]

    dataFlutter = RumahSakit(nama = nama, lokasi = lokasi, alamat = alamat, url_gmaps = url_gmaps, no_telp = no_telp, tersedia = tersedia)

    dataFlutter.save()
    return JsonResponse({
        'message': 'success',
        'nama': nama,
    }, safe=False)

@csrf_exempt
def edit_flutter(request):
    idRS = request.GET['id']
    body = json.loads(request.body)

    nama = body["nama"]
    lokasi = body["lokasi"]
    alamat = body["alamat"]
    url_gmaps = body["url_gmaps"]
    no_telp = body["no_telp"]
    tersedia = body["tersedia"]

    obj = get_object_or_404(RumahSakit, id = idRS)
    obj.nama = nama
    obj.lokasi = lokasi
    obj.alamat = alamat
    obj.url_gmaps = url_gmaps
    obj.no_telp = no_telp
    obj.tersedia = tersedia

    obj.save()
    return JsonResponse({
        'message': 'success',
        'nama': nama,
    }, safe=False)