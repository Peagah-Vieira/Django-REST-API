from rest_framework.viewsets import ModelViewSet

from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer


class CategoriesAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticlesAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer