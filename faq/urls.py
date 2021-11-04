from django.urls import path
from .views import MainView, add_faq

urlpatterns = [
    # path('', MainView, name='index'),
    path('add-faq', add_faq, name='add_faq')
]
