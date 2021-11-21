from django.urls import path

import goodsapp.views as goodsapp

app_name = 'goodsapp'

urlpatterns = [
    path('', goodsapp.GoodsListView.as_view(), name='good_list'),
    path('add_good/', goodsapp.GoodCreateView.as_view(), name='good_add'),
]
