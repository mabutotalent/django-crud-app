from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import FamilyMember


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class FamilyListView(ListView):
    model = FamilyMember
    queryset = FamilyMember.objects.all()
    context_object_name = 'list_family'
    template_name = 'familymember_list.html'


class FamilyCreateView(CreateView):
    model = FamilyMember
    template_name = 'familymember_create.html'
    fields = ['first_name', 'last_name', 'age']
    success_url = reverse_lazy('cbv:list')


class FamilyUpdateView(UpdateView):
    model = FamilyMember
    template_name = 'familymember_update.html'
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('cbv:list')


class FamilyDeleteView(DeleteView):
    model = FamilyMember
    template_name = 'familymember_delete.html'
    success_url = reverse_lazy('cbv:list')
