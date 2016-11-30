from django.conf.urls import url
from . import views#. = current directory


app_name = 'baseball' #allows tag on urls etc
urlpatterns = [
    #/baseball /
    url(r'^$', views.index, name='index'), #sets up home page for each individual app section
    #/baseball/batter_id/^ reps begin $reps end
    url(r'^(?P<batter_id>[0-9]+)/$', views.detail, name='detail'), #<id of an object in db>[0-9]+ reps integers from 0-9 and beyond
    url(r'^new_batter/$', views.new_batter, name='new_batter'),
   # url(r'^edit_batter/(?P<batter_id>\d+)/$', views.edit_batter, name='edit_batter'),
]
#by having name, I can avoid hard coding my urls
# {% csrf_token %} is a security measure in html for django