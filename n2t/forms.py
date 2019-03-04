from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    
    class Meta:
    	model = Note
    	fields = ('COORDINATE', 
    	'H1G',
    	'H1F',
        'H1E',
        'H1D',
        'H1C',
        'M1B',
        'M1A',
        'M1G',
        'M1F',
        'M1E',
        'M1D',
        'M1C',
        'L1B',
        'L1A',
        'L1G',
        'L1F',
        'L1E',
        'L1D',
        'L1C',
        'L2B',
        'L2A',
        'L2G',
        'L2F',)
