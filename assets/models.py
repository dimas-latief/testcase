from django.db import models

# Create your models here.
class Assets(models.Model):
    assets_name = models.CharField(max_length=20)

    def __str__(self):
        return self.assets_name

    class Meta:
        verbose_name_plural = "Assets"