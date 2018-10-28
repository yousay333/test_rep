from django.shortcuts import render


def top(request):
    return render(request, 'tab/top.html')
    
def edit(request):
	return render(request, 'tab/edit.html')