from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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


class NewsEasyView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsEasySerializers


class NewsBodyView(APIView):
    def get(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NewsBodySerializers(news)
        return Response(serializer.data)


def news_page(request, *args, **kwargs):
    return render(request, 'news/news_table.html')
