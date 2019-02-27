from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Note
from . import forms

def top(request):
    #note = get_object_or_404(Note, pk=1)
    d={'form':forms.NoteForm(),}
#    return render(request, 'n2t/top.html', {'note': note})
    return render(request, 'n2t/top.html', d)

    
def edit(request):
	values = request.POST.getlist('note')
	return render(request, 'n2t/edit.html')