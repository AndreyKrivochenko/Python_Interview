from django.urls import path

import goodsapp.views as goodsapp

app_name = 'goodsapp'

urlpatterns = [
    path('', goodsapp.GoodsListView.as_view(), name='good_list'),
    path('category/<int:pk>/', goodsapp.GoodsListView.as_view(), name='good_list_pk'),
    path('add_good/', goodsapp.GoodCreateView.as_view(), name='good_add'),
]
