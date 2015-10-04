#coding: utf-8
from django.db import models

class Categoria(models.Model):
	nome = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name
