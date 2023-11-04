from rest_framework import serializers
from news.models import News


class NewsEasySerializers(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    tag_name = serializers.CharField(source='tag.name')

    class Meta:
        model = News
        fields = ('id', 'title', 'user_name', 'create_at', 'tag_name', 'img')


class NewsBodySerializers(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    tag_name = serializers.CharField(source='tag.name')

    class Meta:
        model = News
        fields = ('id', 'title', 'body', 'user_name', 'create_at', 'tag_name')
