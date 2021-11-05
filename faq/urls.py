from django.urls import path
from .views import add_faq

urlpatterns = [
    path('add-faq', add_faq, name='add_faq')
]
