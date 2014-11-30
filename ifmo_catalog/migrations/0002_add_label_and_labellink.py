# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LabelForCourses'
        db.create_table('ifmo_catalog_labelforcourses', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_of_label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=3000, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ifmo_catalog.LabelForCourses'], unique=True, null=True, blank=True)),
            ('protected', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('ifmo_catalog', ['LabelForCourses'])

        # Adding model 'LabelLink'
        db.create_table('ifmo_catalog_labellink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ifmo_catalog.LabelForCourses'])),
            ('course_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ifmo_catalog', ['LabelLink'])


    def backwards(self, orm):
        # Deleting model 'LabelForCourses'
        db.delete_table('ifmo_catalog_labelforcourses')

        # Deleting model 'LabelLink'
        db.delete_table('ifmo_catalog_labellink')


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