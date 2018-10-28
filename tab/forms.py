from django import forms

from .models import Note

class PostNote(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('H1G', )
