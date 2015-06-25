from django.db import models


class Customer(models.Model):
	cust_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50, blank=True)
	second_name = models.CharField(max_length=50)
	user_name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	place = models.CharField(max_length=200)
	contact_no = models.IntegerField()
	# initial_deposit = models.IntegerField(default=0)
	#joining_date = models.DateTimeField(db_index=True, auto_now_add=True)
	
	def __unicode__(self):
		return '%s' % self.first_name
	
	def get_absolute_url(self):
		return ('view_customer_post', None, { 'slug': self.slug })

'''class LoginForm(forms.ModelForm):
	class Meta:
		 model=Customer.get_absolute_url
		 fields=('user_name','password')'''
	

	
class Account(models.Model):
	acc_no = models.AutoField(primary_key=True)
	# cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	cust_id = models.IntegerField(blank=True)
	acc_type = models.CharField(max_length=10)
	total_balance = models.IntegerField()


	def __unicode__(self):
		return '%s' % self.acc_type


class Transaction(models.Model):
	trans_id = models.AutoField(primary_key=True)
	acc_no = models.ForeignKey(Account)
	available_balance = models.IntegerField(default=0)
	#created_on = models.DateTimeField(db_index=True, auto_now_add=True)
	'''transfer=models.IntegerField(default=0,
								 choices=((1,_('deposit')),
								 	      (2,_('withdraw')),
								 	      ))'''
	def __unicode__(self):
		return '%s' % self.available_balance


'''class Deposit(models.Model):
	trans_id = models.AutoField(primary_key=True)
	acc_no = models.ForeignKey(Account)
	amount = models.IntegerField(default=0)

class Withdraw(models.Model):
	
	trans_id = models.AutoField(primary_key=True)
	acc_no = models.ForeignKey(Account)
	available_balance = models.IntegerField(default=0)'''