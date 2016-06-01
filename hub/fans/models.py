from __future__ import unicode_literals

from django.db import models
import os

class Fan(models.Model):
	raw_code = models.CharField(max_length=250)
	description = models.CharField(max_length=200)
	def __str__(self):
		return self.description
	def toggle(self):
		return os.system("sudo pilight-send -p raw --code=\"" + self.raw_code + "\"") 
	
