from django.urls import path, re_path
from django.conf.urls import url

from orderapp import views

app_name = 'orderapp'
urlpatterns = [
    path('list_555/<city_code>/<order_num>', views.order_list, name='list'),
    path('cencel/<uuid:order_num>', views.cencel_order, name='cencel'),
    re_path(r'^search/(?P<phone>1[357-9][\d]{9})$', views.search, name='search'),
    # re_path(r'^search/(?P<email>\w{0,19})$', views.search)
    # url(r'^list2/(?P<city_code>\w+)/(?P<order_num>\d+)$', views.order_list)
    path('query',views.query)
]
