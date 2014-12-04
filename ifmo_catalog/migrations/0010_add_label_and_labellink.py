# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LabelForCourses.protected'
        db.add_column('ifmo_catalog_labelforcourses', 'protected',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LabelForCourses.protected'
        db.delete_column('ifmo_catalog_labelforcourses', 'protected')


    models = {
        'ifmo_catalog.labelforcourses': {
            'Meta': {'object_name': 'LabelForCourses'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_of_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['ifmo_catalog.LabelForCourses']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'protected_for_add_child': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'protected_for_add_course': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'protected_for_delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'protected_for_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ifmo_catalog.labellink': {
            'Meta': {'object_name': 'LabelLink'},
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.LabelForCourses']"})
        }
    }

    complete_apps = ['ifmo_catalog']