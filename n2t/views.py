from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm
from .models import Note

def top(request):
	notes = Note.objects.order_by('COORDINATE')
	return render(request, 'n2t/top.html', {'notes': notes})


def note_new(request):
	if request.method == "POST":
		form = NoteForm(request.POST)
		if form.is_valid():
			note = form.save(commit=True)
			note.save()
			return redirect(top)
	else:
		form = NoteForm()
	return render(request, "n2t/new.html", {"form": form})

def note_tab(request):
	return render(request, "n2t/tab.html")
	
def note_edit(request):
	
	return
	
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'blog/post_detail.html', {'note': note})