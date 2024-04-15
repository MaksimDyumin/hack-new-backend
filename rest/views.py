from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from .models import Article, Comment
from .serializers import ArticlePreviewSerializer, ArticleSerializer, CommentSerizlizer


class ArticleViewSet(ReadOnlyModelViewSet):
  queryset = Article.objects.all()

  def get_serializer_class(self):
    if self.action == 'list':
      return ArticlePreviewSerializer
    return ArticleSerializer
  
class SubCommentViewSet(mixins.RetrieveModelMixin, GenericViewSet):
  serializer_class = CommentSerizlizer
  def get_queryset(self):
    return Comment.objects.filter(parent_id=self.kwargs['pk'])
  
  def retrieve(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

# Create your views here.
