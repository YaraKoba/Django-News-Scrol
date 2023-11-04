from django import template
from news.models import News

register = template.Library()


@register.inclusion_tag('news/news_cards.html')
def draw_news(tag, request):
    if tag == 'все':
        news = News.objects.all()
    else:
        news = News.objects.filter(tag__name=tag)

    return {'items': list(news), 'tag': tag}
