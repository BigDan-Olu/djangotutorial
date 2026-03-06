from django.urls import path
from . import views
from geeksApp.views import GeeksList  

urlpatterns = [
    path("", views.geeks_view, name="geeks_view"),
    path("", GeeksList.as_view(), name="geeks-list"),
]
