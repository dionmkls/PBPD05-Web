from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .forms import APDForm
from .models import APD

# Create your views here.

def index(request):
    lst_of_apd = APD.objects.all().values()  # TODO Implement this
    response = {'lst_of_apd' : lst_of_apd,}

    return render(request, 'apd_index.html', response)

def json(request):
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