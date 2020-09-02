from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='login'),
    path('logout',views.Logout,name='logout'),

    path('search',views.searchh,name='search'),

    path('dashboard',views.dashboard,name='dashboard'),
    path('add_vehicle',views.add_vehicle,name='add_vehicle'),

    path('manage_invehicle',views.manage_invehicle,name='manage_invehicle'),
    path('view_invehicle/<int:pid>',views.view_invehicle,name='view_invehicle'),

    path('manage_outvehicle',views.manage_outvehicle,name='manage_outvehicle'),
    path('view_outvehicle/<int:pid>',views.view_outvehicle,name='view_outvehicle'),

    path('print_status/<int:pid>',views.print_status,name='print'),

    path('visitors_between_dates',views.visitors_between_dates,name='vbd'),
    path('visitor_between_date_details',views.visitor_between_date_details,name='vbdd'),

    path('add_category',views.add_category,name='add_category'),
    path('manage_category',views.manage_category,name='manage_category'),
    path('delete_category/<int:pid>',views.delete_category,name='delete_category'),

    path('change_password',views.change_password,name='change_password'),
]

