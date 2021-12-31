from django.shortcuts import render, HttpResponseRedirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import APDForm
from .models import APD

# Create your views here.

def index(request):
    lst_of_apd = APD.objects.all().values()
    response = {'lst_of_apd' : lst_of_apd,}

    return render(request, 'apd_index.html', response)

def json_apd(request):
    data = serializers.serialize('json', APD.objects.all())
    return HttpResponse(data, content_type="application/json")

@login_required(login_url = '/admin/login/')
def add_apd(request):
    response = {}

    form = APDForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect('.')

    response['form'] = form
    return render(request, "apd_form.html", response)

# Bagian flutter

@csrf_exempt
def add_apd_flutter(request):
    body = json.loads(request.body)

    jenis = body["jenis"]
    url = body["url"]
    harga = body["harga"]
    gambar = body["gambar"]

    new_data = APD(jenis = jenis, lokasi = url, harga = harga, img_source = gambar)

    new_data.save()

    return JsonResponse({
        "message" : "berhasil",
        "jenis" : jenis,
    }, safe = False)