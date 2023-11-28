from django import forms

class MyForm(forms.Form):

    user_text = forms.CharField(widget=forms.TextInput(
        attrs={ 'placeholder': 'e.g. Hello', 'id': 'encode-input'}
    ))
    #forms.CharField(label='Enter Text', max_length=100, initial='Hello')


