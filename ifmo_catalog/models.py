from django.db import models


class LabelForCourses(models.Model):
    name_of_label = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=2000)
    parent = models.ForeignKey('self', blank=True, null=True)
    protected = models.BooleanField(default=False)
    protected_for_edit = models.BooleanField(default=False)
    protected_for_add_child = models.BooleanField(default=False)
    protected_for_delete = models.BooleanField(default=False)
    protected_for_add_course = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id


class LabelLink(models.Model):
    label_id = models.ForeignKey(LabelForCourses)
    course_id = models.CharField(max_length=100)

    def __unicode__(self):
        return self.id