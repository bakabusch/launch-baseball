from django import forms
from .models import Batter


class BatterForm(forms.ModelForm):
    class Meta:
        model = Batter
        fields = ['player', 'year', 'era', 'gp', 'pa', 'ba', 'ops', 'single', 'two', 'three', 'hr', 'bb', 'ibb',
                  'runs', 'rbi', 'steals', 'ubr', 'wgdp', 'sf', 'hbp', 'wrcplus']
        labels = {'player': 'Player', 'year':'year', 'era': 'era', 'gp':'Games Played', 'pa': 'Plate Appearences', 'ba': 'BA',
                  'ops': 'OPS', 'single': '1B', 'two': '2B', 'three': '3B', 'hr': 'HR', 'bb': 'Walks', 'ibb': 'Intentional BB',
                  'runs': 'Runs', 'rbi': 'RBI', 'steals': 'Steals', 'ubr': 'UBR', 'wgdp': 'wGDP', 'sf': 'Sac Flies',
                  'hbp': 'HBP', 'wrcplus': 'wRC+'}
