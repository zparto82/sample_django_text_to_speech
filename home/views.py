from django.shortcuts import render

from extentions.text_to_speech import text_to_speech
from .forms import InputForm



def index(request):
    context = {}

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            file = text_to_speech(text)
            
            context = {}
            context["audio"] = file
    else:
        context["form"] = InputForm()
    
    return render(request, "home/index.html", context=context)