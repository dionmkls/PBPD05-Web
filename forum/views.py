from django.shortcuts import render
from .models import Forum
from .forms import forumForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    forumforum = Forum.objects.all()
    response = {'forumforum': forumforum}
    return render(request, 'forum.html', response)

def add_forum(request):
    form = forumForm(request.POST or None)
    if form.is_valid and request.method == 'POST':
        form.save()
        return HttpResponseRedirect('/forum')
    context = {'form' : form}
    return render(request, 'forum_form.html', context)

def delete_forum(request, id):
    forum = get_object_or_404(Forum, pk=id)
    forum.delete()
    return HttpResponseRedirect('/forum')

def delete_foruuum(request, id):
    forum = get_object_or_404(Forum, pk=id).delete()
    return HttpResponseRedirect('/forum')
    