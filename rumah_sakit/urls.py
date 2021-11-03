from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, add_rs

urlpatterns = [
    path('', index, name='rs_index'),
    path('add/', add_rs, name="rs_form"),
    path('admin/login', auth_views.LoginView.as_view()),
]