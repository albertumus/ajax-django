from django.urls import path
from core.views import HomePageView, change_fav


urlpatterns = [
    path('', HomePageView.as_view() , name="peliculas_view"),
    path('ajax/change-fav', change_fav, name="change_fav")
]