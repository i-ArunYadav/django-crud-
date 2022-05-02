from django.db import models
# Create your models here.
class Products(models.Model):
	product = models.CharField(max_length = 50)

	def __str__(self):
		return self.product
class Items(models.Model):
	product = models.ForeignKey(Products, on_delete = models.CASCADE)

	item_list = models.CharField(max_length = 50)
	price = models.IntegerField()
	quantity = models.IntegerField()

	def __str__(self):
		return self.item_list