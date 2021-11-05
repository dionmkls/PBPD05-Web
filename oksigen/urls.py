from django.urls import path
from .views import index, add_oksigen, json

urlpatterns = [
    path('', index, name='index'),
    path('add', add_oksigen, name='add_oksigen'),
    path('json', json, name='json')
]