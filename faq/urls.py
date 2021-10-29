from django.urls import path
from .views import index, add_faq

urlpatterns = [
    path('', index, name='index'),
    path('add-faq', add_faq, name='add_faq')
]
