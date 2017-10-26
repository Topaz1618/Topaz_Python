from django.conf.urls import url,include
from monitor import monitor_views
urlpatterns = [
    url(r'agent/config/(\d+)/$',monitor_views.agent_con),
    url(r'agent/put/$',monitor_views.put_data),
]