from django.urls import path
from .views import index, json, add_apd, json_flutter, add_apd_flutter

urlpatterns = [
    path('', index, name='index'),
    path('json/', json, name='json'),
    path('add/', add_apd, name="add"),
    path('json-flutter/', json_flutter, name = 'json_flutter'),
    path('add-apd-flutter/', add_apd_flutter, name='add_apd_flutter'),
    
]
