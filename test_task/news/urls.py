from django.urls import path
from .views import news_table, news_page, api_overview, NewsEasyView, get_news_body, change_likes

urlpatterns = [
    path('news/<slug:menu_item_slug>/', news_table, name='menu'),
    path('news/news/<int:pk>/', news_page, name='post'),

    path('api/', api_overview, name='api_overview'),
    path('api/news/', NewsEasyView.as_view(), name='news-list'),
    path('api/news/<int:pk>/', get_news_body, name='news-body'),
    path('api/news/<int:pk>/change-likes', change_likes, name='change_likes'),
]
