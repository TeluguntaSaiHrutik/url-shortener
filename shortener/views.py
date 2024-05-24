from django.shortcuts import render, redirect, get_object_or_404
from .models import urlDB as urls
from . import utils

# Create your views here.

def homepage_view(request):
    short_url = None
    if request.method == "POST":
        url_given = request.POST['url']
        if urls.objects.filter(url=url_given).exists():
            short_url = urls.objects.get(url=url_given).shortened
            full_short_url = request.build_absolute_uri('/') + short_url
            return render(request, "index.html", {'short_url': full_short_url,"url":"https://"+short_url})
        short_url = utils.generate_short_url()
        while urls.objects.filter(shortened=short_url).exists():
            short_url = utils.generate_short_url()
        obj = urls(url=url_given, shortened=short_url)
        obj.save()
        full_short_url = request.build_absolute_uri('/') + short_url
        return render(request, "index.html", {'short_url': full_short_url,"url":"https://"+short_url})
    return render(request, "index.html", {'short_url': short_url})

def redirecter(request, short_url):
    link = get_object_or_404(urls, shortened=short_url)
    return redirect(link.url)
