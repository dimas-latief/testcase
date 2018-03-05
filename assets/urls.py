from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list-assets', views.listAssets, name='list'),
    # url(r'^request-assets', views.requestAssetsForm, name='requestAssets'),
    path('request-assets/<user_id>/<asset_id>', views.requestAssetsForm, name='requestAssets'),
    url(r'^details/(?P<id>\d+)/$', views.detailAsset, name='detailAsset'),
]