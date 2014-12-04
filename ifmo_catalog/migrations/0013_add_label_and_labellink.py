# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'LabelForCourses', fields ['parent']
        db.delete_unique('ifmo_catalog_labelforcourses', ['parent_id'])


        # Changing field 'LabelForCourses.parent'
        db.alter_column('ifmo_catalog_labelforcourses', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ifmo_catalog.LabelForCourses'], null=True))

    def backwards(self, orm):

        # Changing field 'LabelForCourses.parent'
        db.alter_column('ifmo_catalog_labelforcourses', 'parent_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ifmo_catalog.LabelForCourses'], unique=True, null=True))
        # Adding unique constraint on 'LabelForCourses', fields ['parent']
        db.create_unique('ifmo_catalog_labelforcourses', ['parent_id'])


    models = {
        'ifmo_catalog.labelforcourses': {
            'Meta': {'object_name': 'LabelForCourses'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_of_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.LabelForCourses']", 'null': 'True', 'blank': 'True'}),
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