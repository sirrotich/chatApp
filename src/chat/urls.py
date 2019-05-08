from django.conf.urls import url

from .views import index,room

app_name = 'chat'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]

