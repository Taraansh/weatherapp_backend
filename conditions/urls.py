from conditions import views, converts
from django.urls import path, register_converter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

register_converter(converts.FloatConverter, 'float')
register_converter(converts.DateConverter, 'date')

urlpatterns = [
    path('details/<str:location>/', views.search_current_details, name='search_current_details'),
    path('pastdetails/<str:location>/<date:date>/', views.search_past_details, name='search_past_details'),
    path('futuredetails/<str:location>/<date:date>/', views.search_future_details, name='search_future_details'),
]

urlpatterns += staticfiles_urlpatterns()