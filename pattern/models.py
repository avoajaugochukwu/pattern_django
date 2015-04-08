from django.db import models

# Create your models here.
class Item(models.Model):
	unique_id = models.IntegerField(default=0)
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=1000)
	image_url = models.CharField(max_length=100)