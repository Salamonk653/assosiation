from django.conf.urls import url

from media_gallery.en_views import *

urlpatterns = [
    url(r'^media/gallery/$', GalleeryList.as_view(), name='en_gallery_list'),
    url(r'^media/gallery/album/(?P<slug>[\w-]+)/$', ImageList.as_view(), name='en_album_detail'),
    url(r'^media/gallery/video/$', VideoList.as_view(), name='en_video_list'),
]
