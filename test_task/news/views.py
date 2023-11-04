from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from news.models import News
from news.serializers import NewsEasySerializers, NewsBodySerializers


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'api overview': '/',
        'all news': '/news',
        'Search by Tag': '/?tag=tag_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/news/create',
        'Update': '/news/update/pk',
        'Delete': '/news/item/pk/delete'
    }
    return Response(api_urls)


class NewsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10



class NewsEasyView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-create_at')
    serializer_class = NewsEasySerializers
    pagination_class = NewsPagination



@api_view(['GET'])
def get_news_body(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NewsBodySerializers(news)
    return Response(serializer.data)


def news_page(request, *args, **kwargs):
    return render(request, 'news/news_table.html')
