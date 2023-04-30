
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Articles
from articles.serializers import ArticleSerializer, ArticleCreateSerializer, ArticleCompleteSerializer


# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        todos = Articles.objects.all()
        serializer = ArticleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_id):
        article = get_object_or_404(Articles, id=article_id)
        if request.user == article.user:
            serializer = ArticleCompleteSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("수정불가!", status=status.HTTP_403_FORBIDDEN)        