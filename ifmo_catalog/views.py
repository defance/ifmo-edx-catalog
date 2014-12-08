from django.http import HttpResponse
from edxmako.shortcuts import render_to_response
from ifmo_catalog.models import LabelForCourses
from django.http import Http404

def edit_catalog(request):
    label_list = LabelForCourses.objects.all()
    return render_to_response('edit_catalog.html', {'label_list': label_list})
    

def all_courses(request):
    label_list = LabelForCourses.objects.all()
    return render_to_response('all_courses.html', {'label_list': label_list})


def edit_catalog_handler(request):
    label_list = LabelForCourses.objects.all()
    command = request.POST.get('command')
    if command == 'delete_label':
        label_id = int(request.POST.get('label_id'))
        label1 = label_list[0]
        for label in label_list:
            if not label1.id == label.id:
                if label.parent.id == label_id:
                    label.delete()
        del_obj_root = label_list.get(pk=label_id)
        del_obj_root.delete()
        return HttpResponse(command)
