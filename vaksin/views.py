from django.shortcuts import render
from .models import Vaksin
from .forms import VaksinForm

# Create your views here.
def index(request):
    vaksins = Vaksin.objects.all().values()
    response = {'vaksin': vaksins}
    return render(request, 'index_vaksin.html', response)

def add_vaksin(request):
    form = VaksinForm()

    if request.method == "POST":
        form = VaksinForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(index)
    context = {'form': form}
    return render(request, "form_vaksin.html", context)

