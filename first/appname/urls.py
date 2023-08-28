from django.urls import path
from .views import SliderListView  # Burada SliderListView'ı ekleyin

urlpatterns = [
    # ...
    path('sliders/', SliderListView.as_view(), name='slider-list'),  # SliderListView'ı URL'ye ekleyin
    # ...
]