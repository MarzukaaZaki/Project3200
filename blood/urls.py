from django.urls import path
from blood.views import HomePageView
urlpatterns = [
    path('home/',HomePageView.as_view(),name ='home')
]