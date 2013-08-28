from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

class HelloView(TemplateView):
  template_name = "hello.html"
  
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HelloView.as_view(), name='hello'),
    # Examples:
    # url(r'^$', 'myprj.views.home', name='home'),
    # url(r'^myprj/', include('myprj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
