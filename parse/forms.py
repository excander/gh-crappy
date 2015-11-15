#coding=utf8
from django import forms
import datetime

# class ParseForm(forms.Form):
#     infield = forms.CharField(label='Enter:', max_length=100, required=True)
#     pubdatefrom = forms.DateField(input_formats=['%m/%d/%Y'])
#     pubdateto = forms.DateField(initial=datetime.date.today) 
#     inlist = forms.MultipleChoiceField(label='List:', choices=[(u'карандаш',u'карандаш'), (u'светодиод',u'светодиод')])

class DateInput(forms.DateInput):
    input_type = 'date'
	

class ParseForm(forms.Form):
	pubdatefrom = forms.DateField(widget=DateInput)
	pubdateto = forms.DateField(widget=DateInput)
	inplist = forms.CharField(widget=forms.Textarea)
	file = forms.FileField(required=False)


