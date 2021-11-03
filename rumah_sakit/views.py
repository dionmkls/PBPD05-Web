from django.http import response
from django.shortcuts import redirect, render
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
