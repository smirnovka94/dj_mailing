import random

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from apscheduler.schedulers.blocking import BlockingScheduler

from blogs.models import Blog
from clients.models import Clients
from main.forms import MailingForm

from main.models import Mailing, Logs
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify


# @permission_required('main.view_mailing')
def home(request):
    context = {
        'mailing_list': Mailing.objects.all(),
        'active_mailing_list': Mailing.objects.all().filter(satus='Work'),
        'unique_emails': Clients.objects.all().values('email').distinct(),
        'blogs_list': random.sample(list(Blog.objects.all()), k=3),
        'title': 'Mailing service',

    }
    return render(request, 'main/home.html', context)

class MailingCreateView(PermissionRequiredMixin, CreateView):
    model = Mailing
    # fields = '__all__'
    form_class = MailingForm
    template_name = 'main/main_form.html'
    success_url = reverse_lazy('main:home')
    permission_required = 'main.add_mailing'

    # def get_form_kwargs(self):
    #     kwargs = super(MailingCreateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user.email
    #     return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MailingUpdateView(PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'main/main_form.html'
    permission_required = 'main.change_mailing'

    def form_valid(self, form):
        if form.is_valid():
            new_mail = form.save()
            new_mail.slug = slugify(new_mail.name)
            new_mail.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:view', args=[self.kwargs.get('pk')])

class MailingListView(ListView):
    model = Mailing
    template_name = 'main/main_list.html'
    fields = ('name', 'frequency', 'satus',)


class LogListView(ListView):
    model = Logs
    template_name = 'main/log_list.html'

    # def get_queryset(self):
    #    if self.request.user.is_staff:
    #        return Logs.objects.all()
    #    queryset = Logs.objects.filter(mailing__user = self.request.user)
    #    return queryset

class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'main/main_detail.html'
    fields = '__all__'

class MailingDeleteView(PermissionRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'main/main_confirm_delete.html'
    success_url = reverse_lazy('main:home')
    permission_required = 'main.delete_mailing'