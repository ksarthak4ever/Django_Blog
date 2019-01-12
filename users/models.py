from django.db import models
from django.contrib.auth.models import User
from PIL import Image #importing image from pillow library

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self,*args, **kwargs):
		super().save(*args, **kwargs) #running save method of the parent class i.e once profile is updated saving the picture

		img = Image.open(self.image.path) #this will open the image of the current instance

		if img.height > 300 or img.width >300: #to resize profile image
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)