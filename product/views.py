from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from core.views import OwnerRequiredMixin
from .models import Product


class ProductLV(LoginRequiredMixin, ListView):
    model = Product


class ProductDV(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'image', 'url']
    success_url = reverse_lazy('product:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProductCreateView, self).form_valid(form)


class ProductChangeLV(LoginRequiredMixin, ListView):
    template_name = 'product/product_change_list.html'

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Product
    fields = ['title', 'image', 'url']
    success_url = reverse_lazy('product:index')


class ProductDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product:index')
