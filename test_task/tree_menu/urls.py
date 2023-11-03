from django.urls import path
from .views import index, hello_page

urlpatterns = [
    # Прописываем url для пунктов меню.
    # полe <slug:menu_item_slug> берутся из метода get_url модели MenuItem
    path('main_menu/<slug:menu_item_slug>/', index, name='menu'),
    path('', hello_page, name='hello_page')
]
