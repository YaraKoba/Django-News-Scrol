from django.urls import path
from .views import news_main, news_page, api_overview, NewsPaginationView, NewsStatistics, get_tags, get_news_body, change_likes, create_post, update_post, delete_post

urlpatterns = [
    path('news/<slug:menu_item_slug>/', news_main, name='menu'),
    path('news/news/<int:pk>/', news_page, name='post'),
    

    path('api/', api_overview, name='api_overview'),
    path('api/news/', NewsPaginationView.as_view(), name='news-list'),
    path('api/news/statistics/', NewsStatistics.as_view(), name='news-statistics'),
    path('api/news/tags', get_tags, name='news-tags'),
    path('api/news/create', create_post, name='news-create'),
    path('api/news/<int:pk>/', get_news_body, name='news-body'),
    path('api/news/<int:pk>/update', update_post, name='news-update'),
    path('api/news/<int:pk>/delete', delete_post, name='news-delete'),
    path('api/news/<int:pk>/change-likes', change_likes, name='change_likes'),
]
