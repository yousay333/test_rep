from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Note

def top(request):
    note = get_object_or_404(Note, pk=1)
    return render(request, 'n2t/top.html', {'note': note})
    
def edit(request):
	return render(request, 'n2t/edit.html')