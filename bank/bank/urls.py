from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'loc/'include(sign_in.urls'))
    url(r'^create_acc/',include('create_acc.urls')),
    # url(r'loc/'include(acc_status'))
)