from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import State
from .forms import StateForm

class StateListView(ListView):
    model = State
    template_name = 'state_list.html'

class StateDetailView(DetailView):
    model = State
    template_name = 'state_detail.html'

class StateCreateView(CreateView):
    model = State
    form_class = StateForm
    success_url = reverse_lazy('state-list')
    template_name = 'state_form.html'

class StateUpdateView(UpdateView):
    model = State
    form_class = StateForm
    success_url = reverse_lazy('state-list')
    template_name = 'state_form.html'

class StateDeleteView(DeleteView):
    model = State
    success_url = reverse_lazy('state-list')
