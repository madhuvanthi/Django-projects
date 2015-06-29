from django.db import models


class Account(models.Model):
    accountno = models.AutoField(db_column='accountNo', primary_key=True)  
    customerid = models.IntegerField(db_column='customerId', blank=True, null=True)  
    balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class Customer(models.Model):
    custid = models.AutoField(db_column='custId', primary_key=True)  
    firstname = models.CharField(db_column='firstName', max_length=15, blank=True, null=True)  
    lastname = models.CharField(db_column='lastName', max_length=15, blank=True, null=True)  
    username = models.CharField(db_column='userName', max_length=15, blank=True, null=True)  
    password = models.CharField(max_length=15, blank=True, null=True)
    contactno = models.CharField(db_column='contactNo', max_length=15, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'customer'


class Transaction(models.Model):
    transactionid = models.AutoField(db_column='transactionId', primary_key=True)  
    transactiontype = models.IntegerField(db_column='transactionType', blank=True, null=True)  
    transactionamount = models.IntegerField(db_column='transactionAmount', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'transaction'
