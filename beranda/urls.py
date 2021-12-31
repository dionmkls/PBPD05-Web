from django.urls import path
from .views import index, Covid, get_covid_data, add_covid_data, update_covid_data, delete_covid_data,\
    getVaksinData, jsonAllCovData, createCovidData


urlpatterns = [
    path('', index, name='beranda'),
    path('edit-covid-data/', Covid ,name='edit-covid-data'),
    path('add-covid-data/', add_covid_data ,name='add-covid-data'),
    path('get-covid-data/<id>/', get_covid_data ,name='get-covid-data/data_id'),
    path('edit-covid-data/<id>/update', update_covid_data ,name='update-covid-data/data_id'),
    path('edit-covid-data/<id>/delete', delete_covid_data ,name='delete-covid-data/data_id'),  
    path('getVaksinData/', getVaksinData ,name='getVaksinData'),
    path('jsonAllCovData/', jsonAllCovData ,name='jsonAllCovData'),
    path('createCovidData/', createCovidData ,name='createCovidData'),     
]