from django.shortcuts import render
from .models import Forum
from .forms import forumForm
from django.http.response import HttpResponseRedirect

# Create your views here.

def index(request):
    forums = Forum.objects.all()  
    response = {'forum': forums}
    return render(request, 'forum.html', response)

def add_forum(request):
    form = forumForm(request.POST or None)
    if form.is_valid and request.method == 'POST':
        form.save()
        return HttpResponseRedirect('/forum')
    context = {'form' : form}
    return render(request, 'forum_form.html', context)