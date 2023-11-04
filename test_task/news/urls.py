from django.urls import path
from .views import news_page, api_overview, NewsEasyView, NewsBodyView

urlpatterns = [
    path('news/<slug:menu_item_slug>/', news_page, name='menu'),
    path('api/', api_overview, name='api_overview'),
    path('api/news/', NewsEasyView.as_view(), name='news-list'),
    path('api/news/<int:pk>/', NewsBodyView.as_view(), name='news-body'),
]
