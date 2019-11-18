from django.urls import path 

from .views.trip import home, list_trip, add_trip
from .views.category import list_categories
from .views.employee import list_employees


urlpatterns = [
    path('', home, name="home"),

    # Trip UrlConf
    path('trip/list/', list_trip, name="list_trip"),

    # Category UrlConf
    path('category/list/', list_categories, name="list_categories"),

    # Employee UrlConf
    path('employee/list/', list_employees, name="list_employees"),
    
]
