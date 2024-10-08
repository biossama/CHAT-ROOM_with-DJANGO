from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length=150)


	def __str__(self):
		return self.name


class Room(models.Model):

	host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length = 100)
	description = models.TextField(blank=True, null=True)
	participants = models.ManyToManyField(User, related_name='participants',blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name



class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content
