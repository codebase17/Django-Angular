from django.conf.urls import url
from AddPage import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^AddPage/$',views.AddPageApi)
]