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

# class Employee(models.Model):
#     employee_name = models.CharField(max_length=20)
#     department = models.ForeignKey(Departments, on_delete=models.CASCADE)
#     boss = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)


#     def __str__(self):
#         return self.employee_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, blank=True, null=True)
    boss = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()