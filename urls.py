
from django.conf.urls.defaults import patterns, include, url
from blog.views import hello, current_datetime, hours_ahead, display_meta, search
from blog.blogapp.views import search_form
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,5})/$', hours_ahead),
    ('^display_meta/$', display_meta),
    (r'^search-form/$', search_form),
    (r'^search/$', search),
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
