from django.urls import path

from buyer_tools.views import BuyerSearchView

urlpatterns = [
    path('', BuyerSearchView.as_view(), name="buyersearch"),
]
