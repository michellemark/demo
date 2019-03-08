from django.urls import path, re_path

from buyer_tools.views import PropertySearchView, PropertyDetailView

urlpatterns = [
    re_path(r'property/(?P<mls_id>[0-9]{7})/$', PropertyDetailView.as_view(), name="propertydetail"),
    path('', PropertySearchView.as_view(), name="propertysearch"),
]
