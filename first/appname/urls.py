from django.urls import path,include
from .views import SliderListView, MenuViewSet, MenuItemListCreateView, MenuItemByMenuView, MenuItemDetailView, MenuSelectedItemList   # Burada SliderListView'ı ekleyin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menus', MenuViewSet)

urlpatterns = [
    # ...
    path('sliders/', SliderListView.as_view(), name='slider-list'),  # SliderListView'ı URL'ye ekleyin

    path('menu/', include(router.urls)),
    path('menuitems/', MenuItemListCreateView.as_view(), name='menuitem-list'),
    # Tüm nesneleri sunma için ve yeni öge üretmek
    path('menuitems/menu/<int:menu_id>/', MenuItemByMenuView.as_view(), name='menuitem-by-menu'),
    # Mkullanıcının isteği her hangi bir menünün ögelerini listeler
    path('menuitems/menu/selected/', MenuSelectedItemList.as_view(), name='menuitem-by-menu'),
    # seçili menünün ögeleri listeler
    path('menuitems/<int:pk>/', MenuItemDetailView.as_view(), name='menuitem-detail'),
    # Tekil menu öğelerini sunma için
    # ...
]