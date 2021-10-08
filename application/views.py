from django.shortcuts import render, HttpResponse, redirect
from .models import Url
from django.contrib import messages
from .models import Url
from helper import id_generator
# Create your views here.
def home(request):
    short_url_code = id_generator()
    if request.method == "POST":
        long_url = request.POST.get('long_url')
        url = Url(short_url_code=short_url_code,long_url=long_url)
        url.save()
        messages.success(request, "http://127.0.0.1:8000/"+short_url_code)
    return render(request,"home.html")
def url_redirect(request, short_url_code):
    url_object = Url.objects.get(short_url_code=short_url_code)
    long_url = url_object.long_url
    return redirect(long_url)
    