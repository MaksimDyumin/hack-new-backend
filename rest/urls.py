from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, SubCommentViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, 'article')
router.register('subcomments', SubCommentViewSet, 'subcomment')

urlpatterns = [
  path('', include(router.urls)),
]
