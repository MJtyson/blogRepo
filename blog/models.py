from django.db import models

# Create your models here.
class Blog(models.Model):

	#title for the headlines
	title = models.CharField(max_length = 100, unique =True)
	slug = models.SlufField(max_length = 100,unique =True)
	body = models.TextField()
	posted = models.DateTimeField(db_index = True, auto_now_add = True)
	category = models.ForeignKey('blog.category')

	def __unicode__(self):
		return "%s"%self.title


	def get_absolute_url(self):
		return ('view_blog_post', None, {'slug':self.slug})

class Category(models.Model):

	title = models.CharField(max_length = 100, db_index = True)
	slug = models.SlufField(max_length = 100,db_index =True)

	def __unicode__(self):
		return "%s"%self.title


	def get_absolute_url(self):
		return ('view_blog_category', None, {'slug':self.slug})
