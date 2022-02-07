
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username   = models.CharField(max_length=255, unique=True)
    email       = models.EmailField(max_length=254, unique=True)
    firstname   = models.CharField(max_length=255, unique=True)
    lastname   = models.CharField(max_length=255, unique=True)
    is_admin   = models.BooleanField(default=False) 

    
    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = []
    
    
    class Meta:
        ordering = ["-pk"]




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ["pk"]
    def __str__(self):
        return f'{self.user.username} Profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile
