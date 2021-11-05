from django.urls import path
from .views import index, add_forum, delete_forum

urlpatterns = [
    path('', index, name='index'),
    path('add-forum/', add_forum, name='add_forum'),
    path('delete-forum/<id>',delete_forum, name='delete_forum' )
]