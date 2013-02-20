from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^$', view=index, name='finance_index'),
)

