from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import Context, RequestContext,loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from models import Customer, Account, Transaction


def welcome(request):
	templates=get_template("myprojects/main.html")
 	variables=Context({
 		'head_title' : "BANKING",
 		'page_title' : "welcome",
 		})
 	output=templates.render(variables)
 	return HttpResponse(output)


def addRegistration(request):
	return render(request,"myprojects/reg.html")


def  register(request):
	register = Customer(firstname 	= 	request.POST.get('firstName'),
						lastname 	= 	request.POST.get('lastName'),
						username 	= 	request.POST.get('userName'),
						password 	= 	request.POST.get('password'),
						contactno 	= 	request.POST.get('contactNo'))
	register.save()
	custId = register.custid

	addAccount = Account(customerid = custId,
						 balance= request.POST.get('balance'))

	addAccount.save()
	# cust_id = res[0].id
	# return HttpResponse(cust_id)
	#return render(request,"myprojects/welcome.html")
	t 		= 	get_template("myprojects/sucess.html")
	text 	= 	'Registered Sucessfully'
	c 		= 	RequestContext(request, { 'text' : text } )
	return HttpResponse(t.render(c))


def login(request):
	return render(request,"myprojects/login.html")

def logincheck(request):
	userName=request.POST.get('userName')
	password=request.POST.get('password')
	#return HttpResponse(password)
	checkLogin  = Customer.objects.filter(username=userName,password=password)
	customerId  = int(checkLogin[0].custid)
	
	getBalance = Account.objects.filter(customerid=customerId)
	currentBal = getBalance[0].balance

	templates=get_template("myprojects/trans.html")

	variables=Context({
 		'cust_id' : customerId,
 		'balanceAmt' : currentBal,
 		})
 	output=templates.render(variables)
 	return HttpResponse(output)

def submit(request):

	t 		= 	get_template("myprojects/tsucess.html")
	text 	= 	'Transaction sucess'
	c 		= 	RequestContext(request, { 'text' : text } )
	return HttpResponse(t.render(c))




	# return HttpResponse(balanceAmt)
	#c=Customer.objects.filter(name='madhu',password='water123')
	# return render(request,"myprojects/wel.html")



	# return HttpResponse(currentBal)

	

# def main_page(request):

#  	templates=get_template("myprojects/main.html")
#  	variables=Context({
#  		'head_title' : "BANKING",
#  		'page_title' : "welcome",
#  		})
#  	output=templates.render(variables)
#  	return HttpResponse(output)



# def index(request):
 	
#  	return render(request,"myprojects/login.html")




# def log(request):

# 	user_name=request.POST.get('user_name')
# 	password=request.POST.get('password')
# 	#return HttpResponse(password)
# 	checkLogin  = Customer.objects.filter(user_name=user_name,password=password)
# 	customerId  = int(checkLogin[0].cust_id)
# 	# return HttpResponse(customerId)
# 	cust_id=int(customerId)
# 	# return HttpResponse(cust_id)
# 	getBalance  = Account.objects.filter(cust_id=cust_id)
# 	balanceAmt  = getBalance[0].total_balance


# 	templates=get_template("myprojects/trans.html")

# 	variables=Context({
#  		'cust_id' : cust_id,
#  		'balanceAmt' : balanceAmt,
#  		})
#  	output=templates.render(variables)
#  	return HttpResponse(output)


# 	# return HttpResponse(balanceAmt)
# 	#c=Customer.objects.filter(name='madhu',password='water123')
# 	# return render(request,"myprojects/wel.html")


# def welcome(request):

# 	# return HttpResponse(request.POST.get('firstname'))
# 	res=Customer(	cust_id		=	request.POST.get('cust_id'),
# 					first_name 	= 	request.POST.get('firstname'),
# 					second_name = 	request.POST.get('lastname'),
# 					user_name 	= 	request.POST.get('username'),
# 					password 	= 	request.POST.get('password'),
# 					place 		= 	request.POST.get('place'),
# 					contact_no 	= 	request.POST.get('contact_no'),
# 					acc_no		=	0,
# 					acc_type	=	request.POST.get('acc_type'))
# 	res.save()
# 	# cust_id = res[0].id
# 	# return HttpResponse(cust_id)
# 	#return render(request,"myprojects/welcome.html")
# 	t 		= 	get_template("myprojects/sucess.html")
# 	text 	= 	'Registered Sucessfully'
# 	c 		= 	RequestContext(request, { 'text' : text } )
# 	return HttpResponse(t.render(c))
 	
#  	# return render(request,"myprojects/sucess.html")


 		
# def register(request):
# 	return render(request,"myprojects/reg.html")

	

# '''def create(request):
# 	return render(request,"myprojects/acc.html")

# def account(request):
# 	res=Account(	acc_no			=	request.POST.get('acc_no'),
# 					cust_id			=	11,
# 					acc_type 		= 	request.POST.get('acc_type'),
# 					total_balance	= 	request.POST.get('initial_deposit'))
# 	res.save()
# 	#return render(request,"myprojects/welcome.html")
# 	t 		= 	get_template("myprojects/save.html")
# 	text 	= 	'Account Created'
# 	c 		= 	RequestContext(request, { 'text' : text } )
# 	return HttpResponse(t.render(c))'''


# def transaction(request):
# 	return render(request,"myprojects/trans.html")

# def submit(request):

# 	t 		= 	get_template("myprojects/tsucess.html")
# 	text 	= 	'Transaction sucess'
# 	c 		= 	RequestContext(request, { 'text' : text } )
# 	return HttpResponse(t.render(c))

# def transfer(request):
	
# 	transaction_amount=request.POST.get('transaction_amount')	
# 	if(transaction_type==1):
# 		total_balance=total_balance+transaction_amount
# 	else:
# 		if(total_balance<300):
# 			return HttpResponse('transaction failure')
# 		else:
# 			total_balance=total_balance-transaction_amount
# 			print total_balance



	
	
