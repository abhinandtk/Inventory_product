from django.urls import path
from .views import  *


urlpatterns = [
    path('createproduct',CreateProductview.as_view(),name="createproduct"),
    path('getallproduct',Getproduct.as_view(),name="getallproduct"),
    path('addstock',Addstock.as_view(),name="addstock"),
]
