from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def homepage_042(request):
    name = "108207442"
    return render(request, "homepage_042.html", locals())

def homepage_test(request):
    name = "test"
    return render(request, "homepage_test.html", locals())
def homepage_000(request):
    name = "108207000"
    return render(request, "homepage_000.html", locals())
def homepage_004(request):
    name = "108207004"
    return render(request, "homepage_004.html", locals())
