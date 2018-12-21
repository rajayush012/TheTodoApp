from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

class Todo(models.Model):
    task = models.CharField(max_length=50)
    desc = models.TextField()
    cdate = models.DateField(default=timezone.now())
    due = models.DateField()
    category = models.ForeignKey(Category, default="general",on_delete=models.CASCADE)
