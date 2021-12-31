from django.urls import path
from .views import index, json_apd, add_apd, add_apd_flutter

urlpatterns = [
    path('', index, name='index'),
    path('json/', json_apd, name='json_apd'),
    path('add/', add_apd, name="add"),
    path('add-apd-flutter/', add_apd_flutter, name='add_apd_flutter'),
]
