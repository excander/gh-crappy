from django import forms


class ParseForm(forms.Form):
    infield = forms.CharField(label='Enter:', max_length=100)
