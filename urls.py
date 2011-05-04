from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView
from django.contrib import admin

from Apps.cv.views import *
from Apps.cv.models import *
from Apps.comments.models import Commentaires
from Apps.comments.views import Createcomments


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     url(r'^comment/(?P<pk>\d+)/$', Createcomments.as_view()),
     url(r'^comment/cv/(?P<pk>\d+)/$', DetailView.as_view(
                model = Commentaires,
                template_name = 'Commentaires/commentaire_detail.html')),
     url(r'^cv/$', ListView.as_view(
                model = Info,
                template_name = 'Cv/cv_list.html')),           
     url(r'^cv/(?P<pk>\d+)/$', CvView.as_view()),
     url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),

)



urlpatterns += patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'index.html'}, name='base_index'),
)





from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)