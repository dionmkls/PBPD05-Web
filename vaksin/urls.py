from django.urls import path
from .views import add_vaksin, index

urlpatterns = [
    path('', index, name='index'),
    path('add-location', add_vaksin, name='add_vaksin'),
]
