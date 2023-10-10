from django.shortcuts import render, get_object_or_404

from main.models import Mailing
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

def home(request):
    context = {
        'object_list': Mailing.objects.all(),
        'title': 'Skystore',
        'title_comments': 'Skystore - это отличный вариант выбора товара на любой вкус!'
    }
    return render(request, 'main/home.html', context)



class MailingCreateView(CreateView):
    model = Mailing
    fields = '__all__'
    template_name = 'main/main_form.html'
    success_url = reverse_lazy('main:home')


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['name'] = get_object_or_404(Board, pk=[self.kwargs.get('pk')])
        return context_data

    def form_valid(self, form):
        obj = form.save()
        # send_order_email(obj)
        return super().form_valid(form)

class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'
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

class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'main/main_detail.html'
    fields = '__all__'

class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'main/main_confirm_delete.html'
    success_url = reverse_lazy('main:home')