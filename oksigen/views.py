from django.shortcuts import render
from .models import Oksigen
from .forms import OksigenForm
from django.http import HttpResponseRedirect

def index(request):
    oksigens = Oksigen.objects.all().values()
    response = {'oksigens': oksigens}
    return render(request, 'index.html', response)

def add_oksigen(request):
    context ={}
    form = OksigenForm(request.GET or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/tempat-oksigen')
  
    context['form']= form
    return render(request, "form.html", context)