from django.urls import path 

from .views.trip import home, list_trip, add_trip, create_trip, edit_trip, update_trip
from .views.category import list_categories, add_category, create_category, edit_category, update_category
from .views.employee import list_employees, add_employee, create_employee, edit_employee, update_employee


urlpatterns = [

    # Trip UrlConf
    path('trip/list/', list_trip, name="list_trip"),
    path('trip/add/', add_trip, name="add_trip"),
    path('trip/create/', create_trip, name="create_trip"),
    path('trip/<int:pk>/edit/', edit_trip, name="edit_trip"),
    path('trip/<int:pk>/update/', update_trip, name="update_trip"),

    # Category UrlConf
    path('category/list/', list_categories, name="list_categories"),
    path('category/add/', add_category, name="add_category"),
    path('category/create/', create_category, name="create_category"),
    path('category/<int:pk>/edit/', edit_category, name="edit_category"),
    path('category/<int:pk>/update/', update_category, name="update_category"),

    # Employee UrlConf
    path('employee/list/', list_employees, name="list_employees"),
    path('employee/add/', add_employee, name="add_employee"),
    path('employee/create/', create_employee, name="create_employee"),
    path('employee/<int:pk>/edit/', edit_employee, name="edit_employee"),
    path('employee/<int:pk>/update/', update_employee, name="update_employee"),
    
]
