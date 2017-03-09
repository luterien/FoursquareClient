from django.conf.urls import url

from .views import index, make_foursquare_request


urlpatterns = [

    url(r'^$', index, name="index"),

    url(r'^ajax/make-request/$', make_foursquare_request, name="make-request"),

]

