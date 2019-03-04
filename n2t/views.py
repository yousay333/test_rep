from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm
from .models import Note

def top(request):
	note = get_object_or_404(Note, pk=1)
#	d={'form':forms.NoteForm(),}
	return render(request, 'n2t/top.html', {'note': note})
#   return render(request, 'n2t/top.html', d)


def note_new(request):
	if request.method == "POST":
		note = NoteForm(request.POST)
		if form.is_valid():
			note = form.save(commit=True)
			note.save()
			return render(n2t/top.html, pk=note.pk)
	else:
		form = NoteForm()
	return render(request, "n2t/new.html", {"form": form})

def note_tab(request):
	return render(request, "n2t/tab.html")