from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def parse_view(request): 
    return render(request, 'parse\parse_view.html')
