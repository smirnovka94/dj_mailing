import random
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from blogs.models import Blog
from clients.models import Clients
from main.forms import MailingForm
from main.models import Mailing, Logs, Message
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

def home(request):
    context = {
        'mailing_list': Mailing.objects.all(),
        'active_mailing_list': Mailing.objects.all().filter(satus='Work'),
        'unique_emails': Clients.objects.all().values('email').distinct(),
        'blogs_list': random.sample(list(Blog.objects.all()), k=3),
        'title': 'Mailing service',
        'user_group': str(request.user.groups.values_list('name', flat=True))[10:-1],

    }
    return render(request, 'main/home.html', context)


class MailingCreateView(PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'main/main_form.html'
    success_url = reverse_lazy('main:home')
    permission_required = 'main.add_mailing'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MailingUpdateView(PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'main/main_form.html'
    permission_required = 'main.change_mailing'

    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:view', args=[self.kwargs.get('pk')])


class MailingListView(ListView):
    model = Mailing
    template_name = 'main/main_list.html'
    fields = ('name', 'frequency', 'satus',)

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name__contains="Пользоват").exists():
            return super().get_queryset().filter(user=user)
        else:
            return super().get_queryset()


class LogListView(ListView):
    model = Logs
    template_name = 'main/log_list.html'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'main/main_detail.html'
    fields = '__all__'


class MailingDeleteView(PermissionRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'main/main_confirm_delete.html'
    success_url = reverse_lazy('main:home')
    permission_required = 'main.delete_mailing'


class MessageCreateView(CreateView):
    model = Message
    fields = '__all__'

    template_name = 'main/message_form.html'
    success_url = reverse_lazy('main:home')
    permission_required = 'main.add_message'


class MessageListView(ListView):
    model = Message
    template_name = 'main/message_list.html'
    fields = '__all__'


class  MessageUpdateView(UpdateView):
    model = Message
    template_name = 'main/message_form.html'
    fields = '__all__'


class MessageDeleteView(PermissionRequiredMixin, DeleteView):
    model = Message
    template_name = 'main/message_confirm_delete.html'
    success_url = reverse_lazy('main:home')
    permission_required = 'main.delete_message'