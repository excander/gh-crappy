#coding=utf8
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import ParseForm
from django.http import HttpResponse
from .mainfunc import download_csv
from renamer import latinizator 
import datetime

from .mainfunc import handle_uploaded_file
from .mainfunc import read_inplist, start
from .mainfunc import yesterday, today

##def parse_view(request):
##    form = ParseForm()
##    return render(request, 'parse/parse_view.html', {'form': form})

# def parse_view(request):
#     inp_list = ["asd", "qwe"]
#     if request.method == "POST":
#         form = ParseForm(request.POST)
#         if form.is_valid():
#             infield = form.cleaned_data['infield']
#             # inp_list = form.cleaned_data['inlist']
#             for i, inp_word in enumerate(inp_list):
#                 download_csv(inp_word, i)
#                 print "static/" + str(i) + " " + latinizator(inp_word) + ".csv was successfully downloaded"
#             if infield.isdigit():
#                 f = open("parse/templates/parse/res.html", 'wb')
#                 f.write('''{% extends "parse/base.html" %} {% block content %}''')
#                 for i in range(int(infield)):
#                     f.write("<p>"+str(i)+"</p>")
#                 f.write("{% endblock content %}")
#                 return render(request, 'parse/res.html')
#             else:
#                 return redirect('parse_result', infield=infield)
#     else:
#         data = {'infield': 'hello',
#                 'inlist': [u'карандаш', u'светодиод'],
#                 'pubdatefrom' : datetime.date.today(),
#                 'pubdateto' : datetime.date.today()}
#         form = ParseForm(data)
#     return render(request, 'parse/parse_view.html', {'form': form, 'inlist' : inp_list})



def parse_view(request):
    if request.method == 'POST':
        form = ParseForm(request.POST, request.FILES)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            format = "%d.%m.%Y"
            df = (form.cleaned_data['pubdatefrom']).strftime(format)
            dt = (form.cleaned_data['pubdateto']).strftime(format)
            delta = form.cleaned_data['delta']
        
            if request.FILES:
                handle_uploaded_file(request.FILES['file'])

            # .split('\n')
            start(df, dt, delta)
            return redirect('parse_result', infield="thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        data = {
                    'pubdatefrom' : yesterday(),
                    'pubdateto' : today(),
                    'inplist' : read_inplist(),
                    'delta' : 1,
                }
        form = ParseForm(data)
    return render(request, 'parse/parse_view.html', {'form': form})




def parse_result(request, infield):
    return render(request, 'parse/parse_result.html', {'infield': infield})




def start_parse(request):
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


def download_file(request):
    try:
        f = open(r'parse/files/result_file.csv', 'rb')
        return HttpResponse(f, content_type='application/ms-excel')
    except (IOError, ValueError):
        return redirect('parse_result', infield="file not found")