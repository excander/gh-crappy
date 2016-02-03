# -*- coding: utf8 -*-
from grab import Grab
import urllib
import os
import time
import datetime

path = os.path.abspath(os.path.dirname(__file__))

def download_csv(word,df,dt,sec):
    time.sleep(sec)
    res = urllib.quote(word.encode('utf8'))

    url = "".join([
    	"http://zakupki.gov.ru/epz/order/quicksearch/orderCsvSettings/quickSearch/download.html?",
    	"placeOfSearch=FZ_44&_placeOfSearch=on",
    	"&placeOfSearch=FZ_223&_placeOfSearch=on",
    	"&placeOfSearch=FZ_94&_placeOfSearch=on",
    	"&priceFrom=0",
    	"&priceTo=200+000+000+000",
    	"&publishDateFrom=", df,
    	"&publishDateTo=", dt,
    	"&updateDateFrom=",
    	"&updateDateTo=",
    	"&orderStages=AF&_orderStages=on",
    	"&orderStages=CA&_orderStages=on",
    	"&_orderStages=on&_orderStages=on",
    	"&sortDirection=false",
    	"&sortBy=UPDATE_DATE",
    	"&recordsPerPage=_10",
    	"&pageNo=1",
    	"&searchString=", res,
    	"&strictEqual=false",
    	"&morphology=false",
    	"&showLotsInfo=false",
    	"&isPaging=false",
    	"&isHeaderClick=",
    	"&checkIds=",
    	"&quickSearch=true",
    	"&userId=null",
    	"&conf=true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;"])

    g = Grab()
    g.go(url)
    # g.response.save("static/" + str(num) + ".csv")
    return g.response.body

def yesterday():
	return datetime.date.today() - datetime.timedelta(1)

def today():
	return datetime.date.today()


def handle_uploaded_file(f):
	with open(path +'/input.txt', 'w') as destination:
		for chunk in f.chunks():
			destination.write(chunk)



def read_inplist():
    res_line = ''
    f = open(path + '/input.txt', 'rb')
    for line in f:
        res_line += line
    f.close()
    return unicode(res_line, "utf8")


def save_inplist(inplist):
    f = open(path + '/input.txt', 'w')
    for line in inplist.split("\n"):
        f.write(line.encode("utf8"))
    f.close()


def start(inplist, df, dt, delta):
    import csv
    import xlwt, xlrd

    headstyle = xlwt.easyxf('pattern: pattern solid, fore_color gray25; font: color black, bold 1; align: horiz center, wrap 1; border: top thin, right thin, bottom thin, left thin')
    hyperstyle = xlwt.easyxf('pattern: pattern solid, fore_color white; font: color blue, underline on; border: top no_line')
    colwidth = [4010, 3726, 8192, 25799, 1649, 2616, 3754, 1450, 3840, 3754, 4323, 6257, 3242, 3157, 3896, 4920, 3384, 3413, 2048]

    f = open(path + "/media/result_file.csv", "w")
    for i, inp_word in enumerate(inplist.split('\n')):
        f.write(download_csv(inp_word, df, dt, delta))
        f.write("\n")
    f.close()

    with open(path + '/media/result_file.csv', 'rb') as f:
        wb = xlwt.Workbook(encoding="cp1251")
        ws = wb.add_sheet('data', cell_overwrite_ok=True)
        reader = csv.reader(f, delimiter=';')
        for r, row in enumerate(reader):
            hrow = False;
            for c, val in enumerate(row):
                if (c == 0) and (len(val)==25):
                    hrow = True
                if hrow:
                    ws.write(r, c, val, headstyle)
                elif (c == 1) and (hrow == False) and (val <> ''):
                    click = 'http://zakupki.gov.ru/epz/order/quicksearch/search.html?searchString='+ val[1:].decode('cp1251')
                    ws.write(r, c, xlwt.Formula('HYPERLINK("%s";"%s")' % (click, val.decode(encoding='cp1251'))), hyperstyle)
                else:
                    ws.write(r, c, val)


        for i in range(19):        
            ws.col(i).width = colwidth[i]
        ws.row(0).height_mismatch = True
        ws.row(0).height = 1140 
    wb.save(path + '/media/result_file.xls')

    # with open(path + '/media/result_file.csv', 'rb') as f:
    #     wb = xlwt.Workbook(encoding="cp1251")
    #     ws = wb.add_sheet('data', cell_overwrite_ok=True)
    #     reader = csv.reader(f, delimiter=';')
    #     for r, row in enumerate(reader):
    #         for c, val in enumerate(row):
    #             ws.write(r, c, val)

    #     for i in range(19):        
    #         ws.col(i).width = colwidth[i]
    #     ws.row(0).height_mismatch = True
    #     ws.row(0).height = 1140 

    #     headstyle = xlwt.easyxf('pattern: pattern solid, fore_color gray25; font: color black; align: horiz center"')
        

    # wb.save(path + '/media/result_file.xls')


    
