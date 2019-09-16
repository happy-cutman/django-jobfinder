from django.db import models


class Page(models.Model):
	language = models.CharField(max_length=100)
	city = models.CharField(max_length=100)

	def __str__(self):
		return self.language


class KievPars(models.Model):
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=50)
	descr = models.TimeField(blank=True)
	url = models.CharField(max_length=200)

	def __str__(self):
		return self.title
