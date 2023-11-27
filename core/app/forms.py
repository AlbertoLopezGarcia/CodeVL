from django import forms

class MyForm(forms.Form):

    user_text = forms.CharField(label='Enter Text', max_length=100)


