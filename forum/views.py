from django.shortcuts import render
from .models import Forum
from .forms import forumForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import json

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

def json_flutter(request):
    data = serializers.serialize('json', Forum.objects.all())
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_flutter(request):
    body = json.loads(request.body)

    title = body["title"]
    sender = body["sender"]
    message = body["message"]

    dataFlutter = Forum(ForumTitle = title, ForumFrom = sender, ForumMessage = message)

    dataFlutter.save()
    return JsonResponse({
        "message" : "done",
        "title" : title,
    }, safe = False)

def json(request):
    data = serializers.serialize('json', Forum.objects.all())
    return HttpResponse(data, content_type="application/json")

    