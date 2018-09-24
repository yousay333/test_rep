from django.shortcuts import render


def top(request):
    return render(request, 'tab/top.html')