from django.db import models

class Category(models.Model):
	category = models.CharField(max_length=200)
	def __str__(self):
		return self.category

class MenuItem(models.Model):
	item = models.CharField(max_length=200)
	categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	def __str__(self):
		return self.item

class Demand(models.Model):
	itemId = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1)
	month = models.IntegerField(default=1)
	hour = models.IntegerField(default=0)
	dayType = models.IntegerField(default=0) #0-M, 1-T, 2-W, 3-T, 4-F, 5-S, 6-S/holiday
	supply = models.IntegerField(default=0)
	def __str__(self):
		return str(self.supply)