# -*- coding: utf8 -*-
from grab import Grab
import urllib
import time
import datetime


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
    	"&publishDateTo=14.11.2015", dt,
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
    	"&conf=true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;"])

    g = Grab()
    g.go(url)
    # g.response.save("static/" + str(num) + ".csv")
    return g.response.body

def yesterday():
	return datetime.date.today() - datetime.timedelta(1)

def today():
	return datetime.date.today()


def handle_uploaded_file(f):
	with open(r'parse/input.txt', 'w') as destination:
		for chunk in f.chunks():
			destination.write(chunk)



def read_inplist():
    res_line = ''
    f = open(r'parse/input.txt', 'rb')
    for line in f:
        res_line += line
    f.close()
    return unicode(res_line, "utf8")


def start(df, dt, delta):
	f = open("parse/files/result_file.csv", "w")
	for i, inp_word in enumerate(read_inplist().split('\n')):
		f.write(download_csv(inp_word, df, dt, delta))
		f.write("\n")