from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306245604',
        'name': 'Ignasius Bramantya Widiprasetya',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)