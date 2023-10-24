import os
from django.db import models
from datetime import datetime



def get_image_path(instance, filename):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return os.path.join('sliders/', f'{timestamp}_{filename}')


class Slider(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Menu (models.Model):
    title = models.CharField(max_length=255)
    selected = models.BooleanField(default=False)

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255,blank=True,null=True)
    order = models.PositiveIntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    is_disabled = models.BooleanField(default=False)