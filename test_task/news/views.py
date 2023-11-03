from django.shortcuts import render


def news_page(request, *args, **kwargs):
    return render(request, 'news/news_table.html')
