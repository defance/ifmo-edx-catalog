from django.db import models

class LabelForCourses(models.Model):
    name_of_label = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=3000)
    parent = models.OneToOneField('self', blank = True, null = True)
    def __unicode__(self):
        return self.name_of_label


class LabelLink(models.Model):
    label_id = models.ForeignKey(LabelForCourses)
    course_id = models.CharField(max_length=200)
    def __unicode__(self):
        return self.course_id
