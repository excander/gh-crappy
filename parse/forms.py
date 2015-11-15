#coding=utf8
from django import forms


class ParseForm(forms.Form):
    infield = forms.CharField(label='Enter:', max_length=100, required=True)
    inlist = forms.MultipleChoiceField(label='List:', choices=[(u'карандаш',u'карандаш'), (u'светодиод',u'светодиод')])
