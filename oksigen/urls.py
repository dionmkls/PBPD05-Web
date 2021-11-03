from django.urls import path
from .views import index, add_oksigen

urlpatterns = [
    path('', index, name='index'),
    path('add', add_oksigen, name='add_oksigen')
]