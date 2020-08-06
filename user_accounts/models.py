from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # Create your models here.

# class Profile(models.Model) :
# 	user = models.OneToOneField(user, on_delete=models.CASCADE)
# 	cf_handle = models.CharField(max_length=30)

# @receiver(post_save, sender = User)
# def update_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)
# 	instance.profile.save()
