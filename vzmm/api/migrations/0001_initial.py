# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table(u'api_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('url_path', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'api', ['Email'])


    def backwards(self, orm):
        # Deleting model 'Email'
        db.delete_table(u'api_email')


    models = {
        u'api.email': {
            'Meta': {'object_name': 'Email'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['api']