from rest_framework.serializers import ModelSerializer
from .models import Article, Comment

class ArticlePreviewSerializer(ModelSerializer):
  class Meta:
    model = Article
    fields = ['id', 'headline', 'rating', 'author', 'date']

class CommentSerizlizer(ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id', 'article', 'text', 'parent']

class ArticleSerializer(ModelSerializer):
  comments = CommentSerizlizer(source='get_comments', many=True, read_only=True)

  class Meta:
    model = Article
    fields = ['id', 'headline', 'rating', 'author', 'date', 'text', 'comments']

    

