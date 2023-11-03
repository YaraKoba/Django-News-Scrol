from django.contrib import admin
from news.models import Tag, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'user')
    list_filter = ('user', 'tag',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Tag, TagAdmin)
