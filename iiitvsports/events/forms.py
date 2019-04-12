from django import forms
from events.models import Event,Cricket,Football


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title',)

class CricketForm(forms.ModelForm):
    class Meta:
        model = Cricket
        fields = ('team_name','Player1','Player2',
                    'Player3','Player4','Player5',
                    'Player6','Player7','Player8',
                    'Player9','Player10','Player11')
class FootballForm(forms.ModelForm):
    class Meta:
        model = Football
        fields = ('team_name','Player1','Player2',
                    'Player3','Player4','Player5',
                    'Player6','Player7','Player8',
                    'Player9','Player10','Player11')
