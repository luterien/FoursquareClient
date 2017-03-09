from django.shortcuts import render
from django.http import HttpResponse

from .foursquare import make_request
from .models import Search
from .forms import SearchForm


def index(request):

    return render(
        request, "index.html", {
            'previous_searches': Search.objects.all()[:20],
            'form': SearchForm()}
    )


def make_foursquare_request(request):

    if request.method == "POST":

        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            results = make_request(
                form.cleaned_data["query"], 
                form.cleaned_data["location"]
            )
            return render(request, "make_request.html", {'results': results})

    else:
        return render(request, "make_request.html", {'results': []})

