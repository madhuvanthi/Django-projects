from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.welcome, name="welcome"),
    url(r'^login/$',views.login, name="login"),
    url(r'^addregistration/$',views.addRegistration, name="addRegistration"),
    url(r'^register/$',views.register, name="register"),
    url(r'^logincheck/$',views.logincheck,name="logincheck"),
    url(r'^submit/$',views.submit,name="submit"),
 #    url(r'^$',views.main_page, name="main_page"),
 #    url(r'^register/$', views.register, name="register"),    
	# url(r'^welcome/$', views.welcome, name="welcome"),
 #    url(r'^index/$',views.index, name="index"),
 #    url(r'^log/$',views.log,name="log"),
 #    # url(r'^create/$',views.create,name="create"),
 #    # url(r'^account/$',views.account,name="account"),
 #    url(r'^transaction/$',views.transaction,name="transaction"),
 #    url(r'^submit/$',views.submit,name="submit"),
    #url(r'^deposit/$',views.deposit,name="deposit"),
    #url(r'^withdraw/$',views.withdraw,name="withdraw"),
    )
    # url(r'^welcome$',views.index),'''
  
   
    # (r'^foo/', 'direct_to_template', {'template': 'reg.html'}),
    # Examples:
    # url(r'^$', 'beginner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.index ),
    #url(r'^$', views.index, name='index'),
    
    # url(r'^$',views.main_page, name='main_page' ),
    # url(r'^index/$',views.index),
    # url(r'^welcome/$',views.welcome),	
    # url(r'^register/$' ,views.register),

