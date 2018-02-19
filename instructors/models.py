from django.db import models

# Create your models here.

class Instructor(models.Model):
	#name = models.CharField(max_length=64)
	#surname = models.CharField(max_length=64)
	#course = models.CharField(max_length=64)
	name = models.CharField(verbose_name=u'Instructor Name', max_length=255, help_text = "This is name")
	surname = models.CharField(max_length=255)
	data_of_birth = models.DateField(null=True)
	email =  models.EmailField(unique = True, null=True)
	#phone = models.CharField(max_length=15, null=True, blank=True)
	course = models.CharField(max_length=255, null='True')
	#slug = models.SlugField(unique=True)
	is_active = models.BooleanField(default = True)
	#gender = models.CharField(max_length = 1, choises=('m','Male'), ('f','Female'))