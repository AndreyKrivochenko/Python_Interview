from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from goodsapp.forms import GoodCreateForm
from goodsapp.models import Good


class GoodsListView(ListView):
    template_name = 'goodsapp/goods_list.html'
    queryset = Good.objects.all()
    context_object_name = 'goods_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GoodsListView, self).get_context_data()
        context['title'] = 'Список продуктов'
        return context


class GoodCreateView(CreateView):
    form_class = GoodCreateForm
    model = Good
    template_name = 'goodsapp/goods_add.html'
    success_url = reverse_lazy('goodsapp:good_list')

    def get_context_data(self, **kwargs):
        context = super(GoodCreateView, self).get_context_data()
        context['title'] = 'Добавить продукт'
        return context
