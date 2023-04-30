from rest_framework import serializers
from articles.models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ["title"]        

class ArticleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ["title", "complete"]
 