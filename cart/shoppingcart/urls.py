from django.conf.urls import url
from django.urls import include
from shoppingcart.views import index, book, contact, booking, signup

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^contact$', contact, name='contact'),
    url(r'^booking$', booking, name='booking'),
    url(r'^book/(?P<pk>\d+)$', book, name='book'),
    url(r'^signup$', signup, name='signup'),
]