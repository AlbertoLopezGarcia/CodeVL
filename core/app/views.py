from django.shortcuts import render
from .forms import MyForm
from .coder import encode, decode

def enter_text(request, function=None):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            entered_text = form.cleaned_data['user_text']
            if function == 'encode':
                string = encode(entered_text)
            elif function == 'decode':
                string = decode(entered_text)
            else:
                string = "An error has occurred. Please reload the page and try again."

            return render(request, 'display_text.html', {'string': string})
    else:
        form = MyForm()

    return render(request, 'enter_text.html', {'form': form})