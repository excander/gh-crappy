#! /usr/bin/env python
#coding=utf8

import os,re
from sys import argv

def latinizator(letter):
    dic = {
    ' ':'_',
    ',':'',
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'е':'e',
    'ё':'yo',
    'ж':'zh',
    'з':'z',
    'и':'i',
    'й':'y',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'c',
    'ч':'ch',
    'ш':'sh',
    'щ':'shch',
    'ъ':'y',
    'ы':'y',
    'ь':"'",
    'э':'e',
    'ю':'yu',
    'я':'ya',

    'А':'a',
    'Б':'b',
    'В':'v',
    'Г':'g',
    'Д':'d',
    'Е':'e',
    'Ё':'yo',
    'Ж':'zh',
    'З':'z',
    'И':'i',
    'Й':'y',
    'К':'k',
    'Л':'l',
    'М':'m',
    'Н':'n',
    'О':'o',
    'П':'p',
    'Р':'r',
    'С':'s',
    'Т':'t',
    'У':'u',
    'Ф':'f',
    'Х':'h',
    'Ц':'c',
    'Ч':'ch',
    'Ш':'sh',
    'Щ':'shch',
    'Ъ':'y',
    'Ы':'y',
    'Ь':"'",
    'Э':'e',
    'Ю':'yu',
    'Я':'ya',
    }
    
    for i, j in dic.iteritems():
        letter = letter.replace(i, j)
    return letter


##
##for file_old in os.listdir('.'):
##
##    file_new = latinizator(file_old)
##
##    #Раскомментируйте, чтобы сделать первую букву в имени файла Прописной
##    #file_new = file_new.capitalize()
##
##    if '-p' in argv:
##        print '«{}» будет переименован в «{}»'.format(file_old, file_new)
##    else:
##        print '«{}» переименован в «{}»'.format(file_old, file_new)
##        os.rename(file_old, file_new)
