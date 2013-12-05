# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contacts'
        db.create_table(u'app_t1_contacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app_t1', ['Contacts'])

        # Adding model 'Requests'
        db.create_table(u'app_t1_requests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app_t1', ['Requests'])


    def backwards(self, orm):
        # Deleting model 'Contacts'
        db.delete_table(u'app_t1_contacts')

        # Deleting model 'Requests'
        db.delete_table(u'app_t1_requests')


    models = {
        u'app_t1.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'app_t1.requests': {
            'Meta': {'ordering': "['-time']", 'object_name': 'Requests'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['app_t1']