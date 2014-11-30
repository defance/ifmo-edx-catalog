from django.http import HttpResponse
from edxmako.shortcuts import render_to_response

def edit_catalog(request):
    return render_to_response(edit_catalog.html)


def try1(request):
    return HttpResponse("Hello, world.")