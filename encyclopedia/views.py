from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from . import util

class SearchForm(forms.Form):
    mysearch = forms.CharField(label="New Search")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def wiki(request, page_name):
    if not util.get_entry(page_name):
        return render(request, "encyclopedia/errormessage.html")

    else:
        return render(request, "encyclopedia/entry.html", {
            "entry":util.get_entry(page_name),"title":util.get_title(page_name)
        })


    
