from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from clients.services import get_cache_clients

from clients.forms import ClientsForm
from clients.models import Clients

class ClientCreateView(CreateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('clients:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ClientUpdateView(UpdateView):
    model = Clients
    form_class = ClientsForm

    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('clients:view', args=[self.kwargs.get('pk')])

class ClientListView(ListView):
    model = Clients
    fields = ('email', 'first_name', 'last_name', 'patronymic', 'description',)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        get_cache_clients(self)
        context_data['clients'] = get_cache_clients(self)
        return context_data

class ClientDetailView(DetailView):
    model = Clients
    form_class = ClientsForm

class ClientDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:list')