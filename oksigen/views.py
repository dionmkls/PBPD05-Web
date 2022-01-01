from django.shortcuts import render
from .models import Oksigen
from .forms import OksigenForm
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def index(request):
    oksigens = Oksigen.objects.all().values()
    response = {'oksigens': oksigens}
    return render(request, 'index.html', response)

def json(request):
    data = serializers.serialize('json', Oksigen.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_oksigen(request):
    context ={}
    form = OksigenForm(request.GET or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/tempat-oksigen')
  
    context['form']= form
    return render(request, "form.html", context)