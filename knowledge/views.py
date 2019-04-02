from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from core.views import OwnerRequiredMixin
from .models import Knowledge


# --- ListView
class KnowledgeLV(ListView):
    model = Knowledge
    template_name = 'knowledge/knowledge_all.html'
    context_object_name = 'knowledges'
    paginate_by = 3


# --- DetailView
class KnowledgeDV(DetailView):
    model = Knowledge


# --- PDF View
class KnowledgePV(DetailView):
    model = Knowledge
    template_name = 'knowledge/knowledge_pdf_viewer.html'


class KnowledgeCreateView(LoginRequiredMixin, CreateView):
    model = Knowledge
    fields = ['title', 'slug', 'description', 'content', 'file']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('knowledge:index')

    def form_invalid(self, form):
        return super(KnowledgeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(KnowledgeCreateView, self).form_valid(form)


class KnowledgeChangeLV(LoginRequiredMixin, ListView):
    template_name = 'knowledge/knowledge_change_list.html'

    def get_queryset(self):
        return Knowledge.objects.filter(owner=self.request.user)


class KnowledgeUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Knowledge
    fields = ['title', 'slug', 'description', 'content', 'file']
    success_url = reverse_lazy('knowledge:index')


class KnowledgeDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Knowledge
    success_url = reverse_lazy('knowledge:index')
