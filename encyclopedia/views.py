from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

#class SearchForm(forms.Form):
#   mysearch = forms.CharField(label="Search")

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content" ,widget=forms.Textarea)


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

def search(request):
    query = request.GET.get("q")
    if util.get_entry(query):
        return render(request, "encyclopedia/entry.html", {
            "entry":util.get_entry(query)
        })
    else:
        return render(request, "encyclopedia/search.html", {
            "results":util.get_part_match(query)
        })
    
def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            entries = util.list_entries()

            for entry in entries:
                if entry == title:
                    return render(request, "encyclopedia/errorFileExists.html")
                else:
                    util.save_entry(title, content)
                    #  route to entry
                    return HttpResponseRedirect(f"/wiki/{title}")
        else:
            """
            If form is not valid return display page again and send existing (wrong)
            form data back.
            """
            return render(request, "tasks/add.html", {
                "form":form
            })

    return render(request, "encyclopedia/newpage.html", {
       "form": NewPageForm() 
    })

    