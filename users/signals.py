from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) # signal to create a profile once a user is created
#when a user is saved then send a signal which will be recieved by the decorator receiver and here receiver is create_profile function which has all the arguments which post_save signal passed to it. So we are saying that if the user is created then create a profile object with the user equal to the instance of the User that was created.
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User) #signal to save the profile  
def save_profile(sender, instance, **kwargs): #kwargs just accepts any additional keyword argument onto the end of the function
		instance.profile.save()