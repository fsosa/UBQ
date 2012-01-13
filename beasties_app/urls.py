from django.conf.urls.defaults import *
from django.contrib.auth.views import login

urlpatterns = patterns('beasties_app.views',
    # Examples:
    # url(r'^$', 'ubiqbio.views.home', name='home'),
    # url(r'^ubiqbio/', include('ubiqbio.foo.urls')),
    (r'^$', 'index'),
    (r'^graveyard/$', 'graveyard'),
    (r'^lab/$', 'lab'),
    (r'^level1/$', 'lab'),
    (r'^level2/$', 'lab'),
    (r'^level3/$', 'lab'),
    (r'^fight/$', 'fight'),
    (r'^win_fight/$', 'win_fight'),
    (r'^lose_fight/$', 'lose_fight'),
    (r'^levelup/$', 'levelup'),
    
    (r'^login/$', login), 
    (r'^logout/$', 'logout_page'),
)
