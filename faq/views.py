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
        lower = upper - 3
        faqs = list(FAQ.objects.values()[lower:upper])
        faqs_size = len(FAQ.objects.all())
        size = True if upper >= faqs_size else False
        return JsonResponse({'data': faqs, 'max':size}, safe=False) 

# def index(request):
#     faqs = FAQ.objects.all().values()
#     response = {'faqs': faqs}

#     # paginator = Paginator(faqs, per_page=5)
#     # page_number = request.GET.get('page', 1)
#     # page_obj = paginator.get_page(page_number)

#     return render(
#         request, 
#         'faq.html',
#         response
#         # {
#         #     'faqs': page_obj.object_list,
#         #     'paginator':paginator,
#         #     'page_number':page_number
#         # }
#     )

def add_faq(request):
    context = {}
    form = FAQForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/faq')

    context['form'] = form
    return render(request, 'faq_form.html', context)

# def add_faq(request):
#     context = {}
#     form = FAQForm

#     if request.method == 'POST':
#         question = request.POST['question']
#         answer = request.POST['answer']

#         FAQ.objects.create (
#             question = question,
#             answer = answer
#         )
    
#     context['form'] = form
#     return render(request, 'faq_form.html', context)