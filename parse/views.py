from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import ParseForm

##def parse_view(request):
##    form = ParseForm()
##    return render(request, 'parse/parse_view.html', {'form': form})

def parse_view(request):
    if request.method == "POST":
        form = ParseForm(request.POST)
        if form.is_valid():
            infield = form.cleaned_data['infield']
            return redirect('parse_result', infield=infield)
    else:
        form = ParseForm()
    return render(request, 'parse/parse_view.html', {'form': form})

def parse_result(request, infield):
    return render(request, 'parse/parse_result.html', {'infield': infield})
