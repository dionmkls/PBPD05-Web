from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View, TemplateView
from .forms import FAQForm
from .models import FAQ

class MainView(TemplateView):
    template_name = 'faq.html'

class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_posts')
        lower = upper - 5
        faqs = list(FAQ.objects.values()[lower:upper])
        faqs_size = len(FAQ.objects.all())
        size = True if upper >= faqs_size else False
        return JsonResponse({'data': faqs, 'max':size}, safe=False) 

def add_faq(request):
    context = {}
    form = FAQForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/faq')

    context['form'] = form
    return render(request, 'faq_form.html', context)

def get_flutter():
    faqs = list(FAQ.objects.values())
    return JsonResponse({'data' : faqs})