from django.db import models
import datetime
from PIL import Image 

class users(models.Model):
	mail = models.CharField(max_length=140)
	lname = models.CharField(max_length=140)
	fname = models.CharField(max_length=140)
	code = models.CharField(primary_key=True, max_length=25, unique=True)
	password = models.CharField(max_length=140)
	degree = models.CharField(max_length=140, null=True)
	phone = models.CharField(max_length=140, null=True)
	avatar =models.ImageField(upload_to ='my_app/static/avatar/', null=True, blank=True)
	erhlegch=models.BooleanField(default=False)
	nariin=models.BooleanField(default=False)
	dip=models.BooleanField(default=False)
	tos=models.BooleanField(default=False)
	songoson=models.BooleanField(default=False)
	date=models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return self.code


class research(models.Model):
	res_id=models.AutoField(primary_key=True)
	date=models.DateTimeField(auto_now_add=True, blank=True)
	user_id=models.ForeignKey('users', on_delete=models.CASCADE)
	topic=models.CharField(max_length=255)
	note=models.CharField(max_length=2000)
	def __str__(self):
		return self.topic

class diplom(models.Model):
	d_id=models.AutoField(primary_key=True)
	date=models.DateTimeField(auto_now_add=True, blank=True)
	user_id=models.ForeignKey('users', on_delete=models.CASCADE)
	topic=models.CharField(max_length=255)
	note=models.CharField(max_length=2000)
	check=models.BooleanField(default=False)
	now=models.BooleanField(default=False)
	tosol=models.BooleanField(default=False)
	diplom=models.BooleanField(default=False)
	songoson=models.BooleanField(default=False)
	def __str__(self):
		return self.topic

class detail(models.Model):
	date=models.DateTimeField(auto_now_add=True, blank=True)
	detail_id=models.AutoField(primary_key=True)
	d_id=models.ForeignKey('diplom', on_delete=models.CASCADE)
	st_id=models.ForeignKey('users', on_delete=models.CASCADE)
	tch_id=models.CharField(max_length=140)
	dip=models.BooleanField(default=False)
	tos=models.BooleanField(default=False)
	dun=models.FloatField(null=True)
	def __str__(self):
		return self.tch_id

class plan(models.Model):
	date=models.DateTimeField(auto_now_add=True, blank=True)
	plan_id=models.AutoField(primary_key=True)
	topic=models.CharField(max_length=255)
	note=models.CharField(max_length=2000)
	start_date = models.DateField()
	start_time = models.TimeField(null=True)
	finish_date = models.DateField()
	finish_time = models.TimeField(null=True)
	def __str__(self):
		return self.topic
		
class comments(models.Model):
	date=models.DateTimeField(auto_now_add=True, blank=True)
	comments_id=models.AutoField(primary_key=True)
	user_id=models.ForeignKey('users', on_delete=models.CASCADE)
	note=models.CharField(max_length=2000)
	def __str__(self):
		return self.topic