from django.urls import path
from .views import index, add_forum, delete_forum, add_flutter, json_flutter

urlpatterns = [
    path('', index, name='index'),
    path('add-forum/', add_forum, name='add_forum'),
    path('delete-forum/<id>',delete_forum, name='delete_forum' ),
    path('webservice-forum', add_flutter, name='add_flutter'),
    path('json', json_flutter, name='json'),
]