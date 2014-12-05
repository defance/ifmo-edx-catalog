from django.http import HttpResponse
from edxmako.shortcuts import render_to_response
from ifmo_catalog.models import LabelForCourses


def edit_catalog(request):
    label_list = LabelForCourses.objects.all()
    return render_to_response('edit_catalog.html', {'label_list': label_list})
    

def all_courses(request):
    label_list = LabelForCourses.objects.all()
    return render_to_response('all_courses.html', {'label_list': label_list})


def delete_label(request, id):
    u = LabelForCourses.objects.get(pk=id).delete()

