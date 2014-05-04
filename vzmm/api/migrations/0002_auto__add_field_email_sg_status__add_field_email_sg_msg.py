# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Email.sg_status'
        db.add_column(u'api_email', 'sg_status',
                      self.gf('django.db.models.fields.IntegerField')(default=-1, blank=True),
                      keep_default=False)

        # Adding field 'Email.sg_msg'
        db.add_column(u'api_email', 'sg_msg',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Email.sg_status'
        db.delete_column(u'api_email', 'sg_status')

        # Deleting field 'Email.sg_msg'
        db.delete_column(u'api_email', 'sg_msg')


    models = {
        u'api.email': {
            'Meta': {'object_name': 'Email'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sg_msg': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'sg_status': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'blank': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['api']