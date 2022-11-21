from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def homepage_042(request):
    name = "108207442"
    return render(request, "homepage_042.html", locals())