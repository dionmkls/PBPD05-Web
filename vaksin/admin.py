from django.contrib import admin
from .models import VaksinJakarta, VaksinBogor, VaksinDepok, VaksinTangerang, VaksinBekasi

# Register your models here.
admin.site.register(VaksinJakarta)
admin.site.register(VaksinBogor)
admin.site.register(VaksinDepok)
admin.site.register(VaksinTangerang)
admin.site.register(VaksinBekasi)