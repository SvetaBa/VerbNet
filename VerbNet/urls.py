from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^synsets/$', views.synsets, name='synsets'),
    url(r'^graphs/$', views.graphs, name='graphs'),
    url(r'^verbnet/$', views.verbnet, name='verbnet'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.sendemail, name='contacts'),
    url(r'^synsets/(?P<id>\w+)/$', views.synset, name='synset')
    # url(r'^thanks/$', views.thanks, name='thanks'),
]