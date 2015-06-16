from django.conf.urls import patterns,url
from login import views
#from transaction import views as v2



			url(r'login/?$',views.index, name="index"),
			url(r'login/welcome/?$',views.welcome),
			#@url(r'transaction/?/?$' , v2.index),
)