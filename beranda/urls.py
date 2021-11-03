from django.urls import path
from .views import index, Covid, get_covid_data, add_covid_data, update_covid_data, delete_covid_data, Vaksin, get_vaksin_data, add_vaksin_data,update_vaksin_data, delete_vaksin_data


urlpatterns = [
    path('', index, name='beranda'),
    path('Covid/', Covid ,name='Covid'),
    path('get-covid-data/', get_covid_data ,name='get-covid-data'),
    path('add-covid-data/', add_covid_data ,name='add-covid-data'),
    path('update-covid-data/', update_covid_data ,name='update-covid-data'),
    path('delete-covid-data/', delete_covid_data ,name='delete-covid-data'),

    path('Vaksin/', Vaksin ,name='Vaksin'),
    path('get-vaksin-data/', get_vaksin_data ,name='get-vaksin-data'),
    path('add-vaksin-data/', add_vaksin_data ,name='add-vaksin-data'),
    path('update-vaksin-data/', update_vaksin_data ,name='update-vaksin-data'),
    path('delete-vaksin-data/', delete_vaksin_data ,name='delete-vaksin-data'),
    
    
]

