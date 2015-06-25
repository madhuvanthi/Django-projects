from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import Context, RequestContext,loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from models import Customer, Account




def main_page(request):
 	templates=get_template("myprojects/main.html")
 	variables=Context({
 		'head_title' : "BANKING",
 		'page_title' : "welcome",
 		})
 	output=templates.render(variables)
 	return HttpResponse(output)

def index(request):
 	return render(request,"myprojects/login.html")

def log(request):
	'''r=Customer( user_name=request.POST.get('username'),
				password=request.POST.get('password'))'''

	#c=Customer.objects.filter(name='madhu',password='water123')
	return render(request,"myprojects/wel.html")

	'''user=authenticate(user_name='madhu',password='water123')
	if user is not None:
		if user.is_active:
			print("User is valid")
		else:
			print("Account has been disabled")
	else:
		print(Incorrect username and password)

	r=Customer( user_name=request.POST.get('username'),
				password=request.POST.get('password'))

	if request.method=='POST' :
		form=LoginForm(request.POST)
		if form.is_valid():
			user_name=request.POST.get('username')
			password=request.POST.get('password')
			return render(request,"myprojects/wel.html")
		else:
			return HttpResponseRedirect('main_page')'''
	
def welcome(request):

	# return HttpResponse(request.POST.get('firstname'))
	res=Customer(	cust_id=request.POST.get('cust_id'),
					first_name = request.POST.get('firstname'),
					second_name = request.POST.get('lastname'),
					user_name = request.POST.get('username'),
					password = request.POST.get('password'),
					place = request.POST.get('place'),
					contact_no = request.POST.get('contact_no'))
	res.save()
	#return render(request,"myprojects/welcome.html")
	t = get_template("myprojects/sucess.html")
	text = 'Registered Sucessfully'
	c = RequestContext(request, { 'text' : text } )
	return HttpResponse(t.render(c))
 	
 	# return render(request,"myprojects/sucess.html")
 		
def register(request):
	return render(request,"myprojects/reg.html")
	# return HttpResponse(t.render(c))
	# print request
	

	# res=Customer(cust_id=request.POST.get('cust_id'),
	# 			first_name = request.POST.get('firstname'),
	# 			second_name = request.POST.get('lastname'),
	# 			user_name = request.POST.get('username'),
	# 			password = request.POST.get('password'),
	# 			place = request.POST.get('place'),
	# 			contact_no = request.POST.get('contact_no'))
	# res.save()
	# #return render(request,"myprojects/welcome.html")
	# t = loader.get_template('success.html')
	# text = 'Registered Sucessfully'
	# c = RequestContext(request, { 'text' : text } )
	# return HttpResponse(t.render(c))

def create(request):
	return render(request,"myprojects/acc.html")
def account(request):
	res=Account(	acc_no=request.POST.get('acc_no'),
					cust_id=11,
					acc_type = request.POST.get('acc_type'),
					total_balance = request.POST.get('initial_deposit'))
	res.save()
	#return render(request,"myprojects/welcome.html")
	t = get_template("myprojects/save.html")
	text = 'Account Created'
	c = RequestContext(request, { 'text' : text } )
	return HttpResponse(t.render(c))


def transaction(request):
	return render("myprojects/trans.html")

'''def deposit(request):
	return paass

def withdraw(request):
	return Paass


def withdraw(request):
		return render(request,"myprojects/with.html")
def deposit(request):
		return render(request,"myprojects/depo.html")

	return render(request,"myprojects/reg.html")'''

	
	
