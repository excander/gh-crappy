from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def index_view(request):
    return render(request, 'index/index_view.html')
