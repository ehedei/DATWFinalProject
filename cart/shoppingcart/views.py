from django.shortcuts import render

# Create your views here.
def index(request):
    my_var = "Hola"
    context = {
        'my_var': my_var,
    }
    return render(request, 'index.html', context)