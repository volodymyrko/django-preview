from django.conf.urls.defaults import *
from preview.views import signup, confirm, unsignup

urlpatterns = patterns('',
    url(r'^get-first/$', signup, name = 'preview_signup'),
    url(r'^confirm/$',confirm, name = 'preview_confirm'),
    url(r'^remove/(\w+)/$', unsignup, name = 'preview_unsignup',),
    )
