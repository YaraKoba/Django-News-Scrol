from django.urls import path
from .views import news_page

urlpatterns = [
    path('news/<slug:menu_item_slug>/', news_page, name='menu')
]
