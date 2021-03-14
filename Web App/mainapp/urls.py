from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^service/$', service, name='service'),
    url(r'^registered_categories/$', registered_categories, name='registered_categories'),
    url(r'^new_category/$', new_category, name='new_category'),
    url(r'^items/(?P<value>\w{0,50})/$', items, name='items'),
    url(r'^add_item/$', add_item, name='add_item'),
    url(r'^filtered_items/(?P<value>\w{0,50})/$', filtered_items, name='filtered_items'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
]