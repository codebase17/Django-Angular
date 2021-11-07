from django.conf.urls import url
from ListingPage import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^Listings/$',views.ListingsPageApi)
]