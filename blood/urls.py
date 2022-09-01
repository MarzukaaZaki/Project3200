from django.urls import path
from blood.views import HomePageView, SearchResultsView,map
urlpatterns = [
    path('home/',HomePageView.as_view(),name ='home'),
    path('blood_banks/',map, name='blood_banks'),
    path('find_camp',SearchResultsView.as_view(), name='find_camp')
]