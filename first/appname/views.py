from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Slider
from .serializers import SliderSerializer

class SliderListView(ListAPIView):
    queryset = Slider.objects.filter(is_published=True)
    serializer_class = SliderSerializer
