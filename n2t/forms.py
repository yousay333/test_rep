from django import forms
from .models import Note

NOTE_CHOICES = (
	("H1G", "H1G"),
	("test","test")
)

class NoteForm(forms.ModelForm):
    
    class Meta:
    	model = Note
    note = forms.ChoiceField(
		label="Note",
		widget=forms.CheckboxSelectMultiple,
		choices=NOTE_CHOICES,
		required=True,
	)      