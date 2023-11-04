from django.urls import path
from .views import news_page, api_overview, NewsEasyView, get_news_body

urlpatterns = [
    path('news/<slug:menu_item_slug>/', news_page, name='menu'),
    path('api/', api_overview, name='api_overview'),
    path('api/news/', NewsEasyView.as_view(), name='news-list'),
    path('api/news/<int:pk>/', get_news_body, name='news-body'),
]
