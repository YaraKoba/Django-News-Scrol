from django.shortcuts import render, reverse


def index(request, *args, **kwargs):
    file = 'example_pages/any.html'
    return render(request, file)


def hello_page(request, *args, **kwargs):
    return render(request, 'tree_menu/index.html')
