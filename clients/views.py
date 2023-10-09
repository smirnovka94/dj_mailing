from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from clients.models import Clients

class ClientCreateView(CreateView):
    model = Clients
    fields = '__all__'
    success_url = reverse_lazy('clients:list')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_client = form.save()
    #         new_client.slug = slugify(new_client.title)
    #         new_client.save()
    #     return super().form_valid(form)

class ClientUpdateView(UpdateView):
    model = Clients
    fields = '__all__'

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.slug = slugify(new_client.email)
            new_client.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('clients:view', args=[self.kwargs.get('pk')])

class ClientListView(ListView):
    model = Clients
    fields = ('email', 'name1', 'name2', 'name3', 'description',)

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(category_if=self.kwargs.get('pk'))
    #     return queryset

class ClientDetailView(DetailView):
    model = Clients
    fields = '__all__'

class ClientDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:list')