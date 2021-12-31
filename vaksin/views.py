from django.shortcuts import render, redirect, get_object_or_404
from .models import VaksinJakarta, VaksinBogor, VaksinDepok, VaksinTangerang, VaksinBekasi
from .forms import FormJakarta, FormBogor, FormDepok, FormTangerang, FormBekasi
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def add(request):
    body = json.loads(request.body)
    kkota = body["kota"]
    nnama = body["nama"]
    uurl = body["url"]
    aalamat = body["alamat"]
    ttelp = body["telp"]
    jjenis = body["jenis"]
    ssyarat = body["syarat"]
    

    if kkota == "Jakarta":
        data = VaksinJakarta(nama= nnama, url= uurl, 
                    alamat= aalamat, nomorTelp= ttelp,
                    jenis= jjenis, syaratPeserta= ssyarat)
    elif kkota == "Bogor":
        data = VaksinBogor(nama= nnama, url= uurl, 
                    alamat= aalamat, nomorTelp= ttelp,
                    jenis= jjenis, syaratPeserta= ssyarat)
    elif kkota == "Depok":
        data = VaksinDepok(nama= nnama, url= uurl, 
                    alamat= aalamat, nomorTelp= ttelp,
                    jenis= jjenis, syaratPeserta= ssyarat)
    elif kkota == "Tangerang":
        data = VaksinTangerang(nama= nnama, url= uurl, 
                    alamat= aalamat, nomorTelp= ttelp,
                    jenis= jjenis, syaratPeserta= ssyarat)
    else: # bekasi
        data = VaksinBekasi(nama= nnama, url= uurl, 
                    alamat= aalamat, nomorTelp= ttelp,
                    jenis= jjenis, syaratPeserta= ssyarat)
    
    data.save()

    return JsonResponse({
                'message': 'success',
                'nama': nnama,
            }, safe=False)

def index_flutter(request):
    #bukan dari flutter
    if request.GET['from'] != "flutter":
        return JsonResponse({
                'message': 'Denied',
            }, safe=False)
            
    # tujuan, kota, id
    if request.GET['tujuan'] == "delete":
        return delete_vaksin(request)
    else: # nampilin data
        return JsonResponse(data_to_array(), safe=False)

def index2(request): 
    #nampilin data pake ajax
    if request.is_ajax():
        if request.GET['tujuan'] == "delete":
            print(request)
            return delete_vaksin(request)
        else: # nampilin data
            print('tampil data')
            return JsonResponse(data_to_array(), safe=False)
    
    if request.user.is_authenticated:
        return render(request, 'index_vaksin2.html', {})
    else:
        return render(request, 'index_vaksin.html', {})

def data_to_array():
    vaksinsJak = VaksinJakarta.objects.all().values()
    vaksinsBog = VaksinBogor.objects.all().values()
    vaksinsDep = VaksinDepok.objects.all().values()
    vaksinsTag = VaksinTangerang.objects.all().values()
    vaksinsBek = VaksinBekasi.objects.all().values()

    arr_data = dict()
    arr = []
    for i in vaksinsJak:
        arr += [i]
    arr_data['Jak'] = arr
    
    arr = []
    for i in vaksinsBog:
        arr += [i]
    arr_data['Bog'] = arr
    
    arr = []
    for i in vaksinsDep:
        arr += [i]
    arr_data['Dep'] = arr
    
    arr = []
    for i in vaksinsTag:
        arr += [i]
    arr_data['Tag'] = arr
    
    arr = []
    for i in vaksinsBek:
        arr += [i]
    arr_data['Bek'] = arr


    return arr_data
    
def delete_vaksin(request):
     # ambil data yg mau diapus 
    kota = request.GET['kota']
    id = request.GET['id']

    if kota == "Jakarta":
        obj = get_object_or_404(VaksinJakarta, id = id)
    elif kota == "Bogor":
        obj = get_object_or_404(VaksinBogor, id = id)
    elif kota == "Depok":
        obj = get_object_or_404(VaksinDepok, id = id)
    elif kota == "Tangerang":
        obj = get_object_or_404(VaksinTangerang, id = id)
    elif kota == "Bekasi":
        obj = get_object_or_404(VaksinBekasi, id = id)

    nama = obj.nama
    print(nama + " berhasil di delete")
    # delete object
    obj.delete()

    return JsonResponse({
        'nama': nama
    }, safe=False)
    
@login_required(login_url='/admin/login/')
def add_jakarta(request):
    form = FormJakarta()

    if request.is_ajax():
        form = FormJakarta(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return JsonResponse({
                'message': 'success',
                'nama': request.POST['nama'],
            })
        else:
            print("ga valid")
    else:
        print("bukan ajax")
    context = {'form': form}
    return render(request, "form_jakarta.html", context)

@login_required(login_url='/admin/login/')
def add_bogor(request):
    form = FormBogor()

    if request.is_ajax():
        form = FormBogor(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return JsonResponse({
                'message': 'success',
                'nama': request.POST['nama'],
            })
        else:
            print("ga valid")
    else:
        print("bukan ajax")

    context = {'form': form}
    return render(request, "form_bogor.html", context)

@login_required(login_url='/admin/login/')
def add_depok(request):
    form = FormDepok()

    if request.is_ajax():
        form = FormDepok(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return JsonResponse({
                'message': 'success',
                'nama': request.POST['nama'],
            })
        else:
            print("ga valid")
    else:
        print("bukan ajax")

    context = {'form': form}
    return render(request, "form_depok.html", context)

@login_required(login_url='/admin/login/')
def add_tangerang(request):
    form = FormTangerang()

    if request.is_ajax():
        form = FormTangerang(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return JsonResponse({
                'message': 'success',
                'nama': request.POST['nama'],
            })
        else:
            print("ga valid")
    else:
        print("bukan ajax")

    context = {'form': form}
    return render(request, "form_tangerang.html", context)

@login_required(login_url='/admin/login/')
def add_bekasi(request):
    form = FormBekasi()

    if request.is_ajax():
        form = FormBekasi(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return JsonResponse({
                'message': 'success',
                'nama': request.POST['nama'],
            })
        else:
            print("ga valid")
    else:
        print("bukan ajax")

    context = {'form': form}
    return render(request, "form_bekasi.html", context)
