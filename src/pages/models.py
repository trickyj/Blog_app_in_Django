from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default_2.png', blank=True)
	author = models.ForeignKey(User,default=None, on_delete=models.PROTECT)

	#model method to convert object into strings.

	def __str__ (self):
		return self.title

	#model method to display limited text on the page.

	def snippet(self):
		return self.body[:50] +'...'
