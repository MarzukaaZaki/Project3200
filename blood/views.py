from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import folium
from django.db.models import Q

from blood.models import Blood_Camp

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def map(request):
    m = folium.Map(location=[24.3735039,88.5872464], zoom_start=15)
    folium.Marker(location=[24.3735039,88.5872464]).add_to(m)
    m = m._repr_html_
    context ={'m':m}
    return render(request,'blood_banks.html',context)

class SearchResultsView(ListView):
    model = Blood_Camp
    template_name = 'find_camp.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Blood_Camp.objects.filter(
            Q(name_of_camp__icontains=query) | Q(location__icontains=query)
        )
        return object_list