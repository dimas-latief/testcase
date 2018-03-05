from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Assets(models.Model):
    assets_name = models.CharField(max_length=20)

    def __str__(self):
        return self.assets_name

    class Meta:
        verbose_name_plural = "Assets"

class Departments(models.Model):
    department_name = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name_plural = "Departments"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, blank=True, null=True)
    boss = models.ForeignKey(User, related_name='boss_set', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class AssigningAsset(models.Model):
    status = models.CharField(max_length=20, default="Booked Asset")
    requester = models.ForeignKey(User, related_name='requester_set', on_delete=models.CASCADE)
    approver = models.ForeignKey(User, related_name='approver_set', on_delete=models.CASCADE, blank=True, null=True)
    assets = models.ForeignKey(Assets, on_delete=models.CASCADE)
    quantity = models.IntegerField(default= 0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()