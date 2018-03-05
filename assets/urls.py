from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list-assets', views.listAssets, name='list'),

    path('request-assets/<asset_id>', views.requestAssetsForm, name='requestAssets'),
    url(r'^details/(?P<id>\d+)/$', views.detailAsset, name='detailAsset'),

    path('needApproval/<user_id>', views.requestAssetsApproval, name='requestAssetsApproval'),
    path('approvedRequestedAsset/<assign_assets_id>', views.approvedRequestedAsset, name='approvedRequestedAsset'),

]