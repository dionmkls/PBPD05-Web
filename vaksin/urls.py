from django.urls import path
from .views import add_jakarta, add_bekasi, add_bogor, add_depok, add_tangerang, index2, add, index_flutter

urlpatterns = [
    path('', index2, name='index2'),
    path('add-vaksin-jakarta', add_jakarta, name='add_jakarta'),
    path('add-vaksin-bogor', add_bogor, name='add_bogor'),
    path('add-vaksin-depok', add_depok, name='add_depok'),
    path('add-vaksin-tangerang', add_tangerang, name='add_tangerang'),
    path('add-vaksin-bekasi', add_bekasi, name='add_bekasi'),
    path('add', add, name="add"),
    path('flutter-web-service', index_flutter, name='index_flutter'),
]
