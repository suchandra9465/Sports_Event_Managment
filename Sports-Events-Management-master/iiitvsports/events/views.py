from django.shortcuts import render,get_object_or_404,redirect
from . models import Event,Cricket,Football
from . forms import CricketForm,EventForm,FootballForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                    DetailView,UpdateView,
                                    DeleteView,CreateView)
from braces.views import SelectRelatedMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()

class EventListView(ListView):
    model = Event

class CreateEvent(LoginRequiredMixin, SelectRelatedMixin,CreateView):
    model = Event
    form_class = EventForm

class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event

class CricketListView(LoginRequiredMixin,ListView):
    model = Cricket
    context_object_name = 'crickets'
    template_name = 'cricket_list.html'

    def get_context_data(self, **kwargs):
        kwargs['event'] = self.event
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs.get('pk'))
        queryset = self.event.crickets.order_by('created_at')
        return queryset

class FootballListView(LoginRequiredMixin,ListView):
    model = Football
    context_object_name = 'footballs'
    template_name = 'football_list.html'

    def get_context_data(self, **kwargs):
        kwargs['event'] = self.event
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs.get('pk'))
        queryset = self.event.footballs.order_by('created_at')
        return queryset



######################

@login_required
def add_team_cricket(request,pk):
    event = get_object_or_404(Event,pk=pk)
    user = request.user
    if request.method == 'POST':
        form = CricketForm(request.POST)

        if form.is_valid():
            team = form.save(commit=False)
            team.event = event
            team.created_by = user
            team.save()
            return redirect('home')
    else:
        form = CricketForm()

    return render(request,'events/cricket_form.html',{'form':form})

@login_required
def add_team_football(request,pk):
    event = get_object_or_404(Event,pk=pk)
    user = request.user
    if request.method == 'POST':
        form = FootballForm(request.POST)

        if form.is_valid():
            team = form.save(commit=False)
            team.event = event
            team.created_by = user
            team.save()
            return redirect('home')
    else:
        form = FootballForm()

    return render(request,'events/football_form.html',{'form':form})


class CricketUpdateView(LoginRequiredMixin,UpdateView):
    model = Cricket
    fields = ('Player1','Player2','Player3','Player4',
                'Player5','Player6','Player7','Player8',
                'Player9','Player10','Player11',  )
    template_name = 'events/edit_cricket.html'
    pk_url_kwarg = 'cricket_pk'
    context_object_name = 'cricket'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('home')

class FootballUpdateView(LoginRequiredMixin,UpdateView):
    model = Football
    fields = ('Player1','Player2','Player3','Player4',
                'Player5','Player6','Player7','Player8',
                'Player9','Player10','Player11',  )
    template_name = 'events/edit_football.html'
    pk_url_kwarg = 'football_pk'
    context_object_name = 'football'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('home')
