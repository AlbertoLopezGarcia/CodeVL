from django.shortcuts import render
from .forms import MyForm
from .coder import encode

def enter_text(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            entered_text = form.cleaned_data['user_text']
            encoded_str = encode(entered_text)
            return render(request, 'display_text.html', {'encoded_str': encoded_str})
    else:
        form = MyForm()

    return render(request, 'enter_text.html', {'form': form})
