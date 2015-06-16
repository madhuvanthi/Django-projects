from django.db import models
	
class Auth(models.Model):
	cust_name=models.CharField(max_length=200)
	#acc_no=models.IntegerField(max_length=200)
	passwd=models.CharField(max_length=20)
	def __unicode__(self):
		return self.cust_name

# Create your models here.
