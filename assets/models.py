from django.db import models

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

class Employee(models.Model):
    employee_name = models.CharField(max_length=20)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    # boss = models.ForeignKey("self", on_delete=models.CASCADE, default='')
    boss = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.employee_name