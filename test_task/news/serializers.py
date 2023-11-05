from rest_framework import serializers
from news.models import News, Tag


class NewsEasySerializers(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    tags = serializers.SerializerMethodField()
    create_at = serializers.DateTimeField(format="%d.%m.%y %H:%M")

    class Meta:
        model = News
        fields = ('id', 'title', 'user_name', 'create_at', 'tags', 'img')

    def get_tags(self, obj):
        return [tag.name for tag in obj.tag.all()]


class NewsBodySerializers(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    tags = serializers.SerializerMethodField()
    create_at = serializers.DateTimeField(format="%d.%m.%y %H:%M")

    class Meta:
        model = News
        fields = ('id', 'title', 'body', 'user_name', 'create_at', 'tags', 'likes', 'dislikes')

    def get_tags(self, obj):
        return [tag.name for tag in obj.tag.all()]


class NewsLikesSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'likes', 'dislikes')


class TagSerializers(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    
    class Meta:
        model = Tag
        fields = ('tags',)

    def get_tags(self, obj):
        return [tag.name for tag in obj.all()]