from django import forms
		
		class LoginForm(forms.Form):
			cust_name = forms.CharField(max_length = 100)
			acc_no=forms.IntegerField(max_length=100)
			password = forms.CharField(widget = forms.PasswordInput())