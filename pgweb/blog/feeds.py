from django.contrib.syndication.views import Feed
from models import BlogPost

class LatestPosts(Feed):
  title = "Command Prompt Latest Posts"
  link = "/"
  
  def items(self):
    return BlogPost.objects.all()

  def item_title(self, item):
    return item.title

  def item_description(self, item):
    return item.body
