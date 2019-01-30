from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors= {}
		#names < 2
		if (len(postData['first_name']) < 2) or (len(postData['last_name']) < 2) or (len(postData['email']) < 1):
			errors["blank"]= "Please fill in all required fields."
		# first and last names with numbers
		if not (postData['first_name'].isalpha() and postData['last_name'].isalpha()):
			errors["alpha"]= "Names must not contain numbers."
		# doesnt match email pattern
		if not EMAIL_REGEX.match(postData['email']):
			errors["email"]= "Email address is invalid."
		return errors

class User(models.Model):
	first_name= models.CharField(max_length= 255)
	last_name= models.CharField(max_length= 255)
	email= models.EmailField()
	password=models.CharField(max_length= 255)
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	objects= UserManager()


def __unicode__(self):
	return "id: " + str(self.id) + ", first_name: " + self.first_name + \
    ", last_name: " + self.last_name + ", email: " + self.email + \
    ", password: " + self.password
   

