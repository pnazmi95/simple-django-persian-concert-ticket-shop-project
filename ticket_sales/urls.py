from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'ticket_sales'
urlpatterns = [
    path("concert/list", concert_list_view, name='concert_list_view'),
    path('location/list', login_required(LocationListView.as_view()), name='location_list_view'),
    path('concert/<int:concert_id>', login_required(ConcertDetailsView.as_view()), name='concert_detail_view'),
    path('time/list', login_required(TimeView.as_view()), name='time_view'),
    path('concert_edit/<int:concert_id>', login_required(ConcertEditView.as_view()), name='concert_edit_view'),
]
