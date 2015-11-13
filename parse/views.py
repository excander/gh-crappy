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
            if infield.isdigit():
                f = open("parse/templates/parse/res.html", 'w')
                f.write('''{% extends "parse/base.html" %} {% block content %}''')
                for i in range(int(infield)):
                    f.write("<p>"+str(i)+"</p>")
                f.write("{% endblock content %}")
                f.close()
                return render(request, 'parse/res.html')
            else:
                return redirect('parse_result', infield=infield)
    else:
        form = ParseForm()
    return render(request, 'parse/parse_view.html', {'form': form})

def parse_result(request, infield):
    return render(request, 'parse/parse_result.html', {'infield': infield})

def start_parse(request):
    from django.http import HttpResponse
    from grab import Grab
    from grab.tools.lxml_tools import drop_node
    import xlwt
    from datetime import datetime

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xls'

    url = 'http://zakupki.gov.ru/epz/order/quicksearch/update.html?placeOfSearch=FZ_44&_placeOfSearch=on&placeOfSearch=FZ_223&\
            _placeOfSearch=on&placeOfSearch=FZ_94&_placeOfSearch=on&priceFrom=0&priceTo=200+000+000+000&publishDateFrom=&\
            publishDateTo=&updateDateFrom=&updateDateTo=&orderStages=AF&_orderStages=on&orderStages=CA&_orderStages=on&\
            _orderStages=on&_orderStages=on&sortDirection=false&sortBy=UPDATE_DATE&recordsPerPage=_10&pageNo=1&searchString=&\
            strictEqual=false&morphology=false&showLotsInfo=false&isPaging=true&isHeaderClick=&checkIds='
    xpath = '//td[@class="descriptTenderTd"]//dd[a][2]'

    g = Grab()
    g.go(url)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
        num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')


    page = g.doc.select(xpath)
    for i, element in enumerate(page):
        ws.write(i, 0, i)
        ws.write(i, 1, element.text())

##    wb.save('parse/grabparser/example.xls')
    wb.save(response)
    return response
