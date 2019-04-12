from django.conf.urls import url

from . import views

app_name = 'events'

urlpatterns = [
    url(r'^$',views.EventListView.as_view(),name='event_list'),
    url(r'^new/$',views.CreateEvent.as_view(),name="create"),
    url(r'^(?P<pk>\d+)/$',views.EventDetailView.as_view(),name='event_detail'),
    url(r'^(?P<pk>\d+)/cricket/$',views.CricketListView.as_view(),name = 'cricket_list'),
    url(r'^(?P<pk>\d+)/football/$',views.FootballListView.as_view(),name = 'football_list'),
    url(r'^(?P<pk>\d+)/cricket/new/$',views.add_team_cricket,name = 'add_team_cricket'),
    url(r'^(?P<pk>\d+)/football/new/$',views.add_team_football,name = 'add_team_football'),
    url(r'^(?P<pk>\d+)/cricket/(?P<cricket_pk>\d+)/edit/$',views.CricketUpdateView.as_view(),name = 'cricket_edit'),
    url(r'^(?P<pk>\d+)/football/(?P<football_pk>\d+)/edit/$',views.FootballUpdateView.as_view(),name = 'football_edit'),
]
