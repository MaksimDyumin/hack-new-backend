from django.db import models


class Article(models.Model):
  headline = models.CharField(max_length=255)
  date = models.DateField(auto_now_add=True)
  author = models.CharField(max_length=255)
  text = models.TextField()
  rating = models.IntegerField()

  def get_comments(self):
    return self.comments.filter(parent__isnull=True)

  
class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  text = models.TextField()
  parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='comments') 