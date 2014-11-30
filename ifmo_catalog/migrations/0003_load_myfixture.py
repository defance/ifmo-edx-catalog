# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):


    def forwards(self, orm):
        from django.core.management import call_command
        call_command("loaddata", "main_labels.json")


    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'ifmo_catalog.labelforcourses': {
            'Meta': {'object_name': 'LabelForCourses'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '3000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_of_label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['ifmo_catalog.LabelForCourses']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'ifmo_catalog.labellink': {
            'Meta': {'object_name': 'LabelLink'},
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.LabelForCourses']"})
        }
    }

    complete_apps = ['ifmo_catalog']
    symmetrical = True
