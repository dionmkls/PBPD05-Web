from django.urls import path
from .views import index, get_covid_data, add_covid_data, update_covid_data, delete_covid_data


urlpatterns = [
    path('', index, name='beranda'),
    path('edit-covid-data/', add_covid_data ,name='edit-covid-data'),
    path('add-covid-data/', add_covid_data ,name='add-covid-data'),
    path('get-covid-data/<id>/', get_covid_data ,name='get-covid-data/data_id'),
    path('update-covid-data/<id>/', update_covid_data ,name='update-covid-data/data_id'),
    path('delete-covid-data/<id>/', delete_covid_data ,name='delete-covid-data/data_id'),   
]