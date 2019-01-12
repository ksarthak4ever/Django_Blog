from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # as User is a seperate table and django created that in location django.contrib.auth.models
from django.urls import reverse


class Post(models.Model):  #in django ORM(Object-Relational Mapping) the database structure  can be represented as classes and those classes are called models
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now) #To store the date and time at which the post was created if we used (auto_now=True) this will update date and time every time the post is updated
	 															#or use (auto_now_add=True) this will store date and time only when the post was created but we cant update the date posted so we use timezone
	author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete = models.CASCADE tells django that if the user is deleted then remove all the posts made by him

	def __str__(self): #dunder(i.e double underscore) str method is used to make posts readable in the python shell where we acess the database
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk}) #not using redirect function as here we simply want the url as a string and let django do the rest so we use reverse function



