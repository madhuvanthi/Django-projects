from django.db import models

#from django.db.models import permalink
class Customer(models.Model):
    cust_id = models.IntegerField()
    first_name = models.CharField(max_length=10)
    second_name = models.CharField(max_length=10)
    acc_no = models.IntegerField()
    address = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    #account=models.ForeignKey('customer.account')
    def __unicode__(self):
        return '%s' %self.acc_no
    def get_absolute_url(self):
        return ('view_customer_post', None, { 'slug': self.slug })

    
class Account(models.Model):
    acc_no = models.IntegerField()
    acc_type = models.CharField(max_length=10)
    def __unicode__(self):
        return '%s' %self.acc_type
    #def get_absolute_url(self):
      #  return ('view_customer_account', None, { 'slug': self.slug })

class Transaction(models.Model):
    acc_no=models.IntegerField()
    total_balance=models.IntegerField()
    last_transaction=models.DateTimeField(db_index=True, auto_now_add=True)
    def __unicode__(self):
        return '%s' %self.total_balance
    

    
   


