"""PBP_D5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from hello_world.views import index 

import hello_world.urls as index_urls
import vaksin.urls as vaksin_urls
import apd.urls as apd_urls
<<<<<<< HEAD
=======
import faq.urls as faq_urls
import forum.urls as forum_urls
>>>>>>> a4d92c5d283d16573b439ee96112b63ffd29e344

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", include(index_urls)),
    re_path(r"^$", index, name="index"),
<<<<<<< HEAD
    path('lokasi-vaksin', include(vaksin_urls)),
    path('apd/', include(apd_urls)),
=======
    path('lokasi-vaksin/', include(vaksin_urls)),
    path('beranda/', include('beranda.urls')),
    path('apd/', include(apd_urls)),
    path('faq/', include(faq_urls)),
    path('forum/', include('forum.urls')),
    path('rumah-sakit/', include('rumah_sakit.urls')),
    path('tempat-oksigen/', include('oksigen.urls')),
>>>>>>> a4d92c5d283d16573b439ee96112b63ffd29e344
]
