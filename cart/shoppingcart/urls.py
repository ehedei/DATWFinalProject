from django.conf.urls import url
from shoppingcart.views import index

urlpatterns = [
    url(r'^$', index, name = 'index')
]