from django.shortcuts import render, get_object_or_404
from apscheduler.schedulers.blocking import BlockingScheduler
from main.forms import MailingForm
from main.management.commands.runapscheduler import Command
from main.models import Mailing, Logs
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from main.services import my_job


def home(request):
    context = {
        'object_list': Mailing.objects.all(),
        'title': 'Пользователь',
        'title_comments': 'Skystore - это отличный вариант выбора товара на любой вкус!'
    }
    return render(request, 'main/home.html', context)



class MailingCreateView(CreateView):
    model = Mailing
    fields = '__all__'
    # form_class = MailingForm
    template_name = 'main/main_form.html'
    success_url = reverse_lazy('main:home')


    # def get_form_kwargs(self):
    #     kwargs = super(MailingCreateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

    def form_valid(self, form):
        if form.is_valid():
            new_mail = form.save()
            new_mail.slug = slugify(new_mail.name)
            new_mail.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'main/main_form.html'

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
    template_name = 'main/home.html'
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

class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'main/main_confirm_delete.html'
    success_url = reverse_lazy('main:home')