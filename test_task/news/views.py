from django.shortcuts import render
from rest_framework import generics, status, serializers
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from news.utils import update_likes
from news.models import News
from news.serializers import NewsEasySerializers, NewsBodySerializers, NewsLikesSerializers


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'api overview': '/',
        'Pagination news': 'news/?tags=tag1,tag2,tag3',
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


class NewsPaginationView(generics.ListAPIView):
    serializer_class = NewsEasySerializers
    pagination_class = NewsPagination

    def get_queryset(self):
        queryset = News.objects.all().order_by('-create_at')
        tags_param = self.request.query_params.get('tags', None)

        if tags_param:
            tags = tags_param.split(',')  # Разделяем теги по запятым
            queryset = queryset.filter(tag__name__in=tags).distinct()

        return queryset


@api_view(['GET'])
def get_news_body(request: Request, pk: int):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NewsBodySerializers(news)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request: Request):
    new_post = NewsBodySerializers(data=request.data)

    if News.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if new_post.is_valid():
        new_post.save()
        return Response(new_post.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_post(request: Request, pk):
    try:
        post = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    update_data = NewsBodySerializers(instance=post, data=request.data)

    if update_data.is_valid():
        update_data.save()
        return Response(update_data.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    post.delete()
    return Response(status=status.HTTP_202_ACCEPTED)



@api_view(['POST'])
def change_likes(request: Request, pk):
    data = request.data

    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if 'likes' in data or 'dislikes' in data:
        if 'likes' in data and data['likes'] == 'plus':
            news.likes += 1
        elif 'likes' in data and data['likes'] == 'minus':
            news.likes -= 1
        
        if 'dislikes' in data and data['dislikes'] == 'plus':
            news.dislikes += 1
        elif 'dislikes' in data and data['dislikes'] == 'minus':
            news.dislikes -= 1

        news.save()
        serializer = NewsLikesSerializers(news)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

def news_table(request, *args, **kwargs):
    return render(request, 'news/news_table.html')


def news_page(request, *args, **kwargs):
    return render(request, 'news/news_post.html')
