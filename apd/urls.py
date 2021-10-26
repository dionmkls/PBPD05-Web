from django.urls import path
from .views import index, json, add_apd

urlpatterns = [
    path('', index, name='index'),
    path('json/', json, name='json'),
    path('add/', add_apd, name="add"),
    
]
