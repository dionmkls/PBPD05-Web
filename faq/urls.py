from django.urls import path
from .views import add_faq, get_flutter

urlpatterns = [
    path('add-faq', add_faq, name='add_faq'),
    path('get-flutter', get_flutter, name='get_flutter')
]