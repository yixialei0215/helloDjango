from django.urls import path

from mainapp.user_v import find_fruit, delete_cookie
from mainapp.views import user_list, user_list2, user_list3, add_user, update_user, delete_user, find_store, \
    all_store, count_fruit, delete_fruit

urlpatterns = [
    path('list', user_list3),
    path('add', add_user),
    path('update', update_user),
    path('delete', delete_cookie),
    path('find', find_fruit),
    path('store', find_store),
    path('store_all', all_store),
    path('count', count_fruit),
    path('deletefruit', delete_fruit),
]
