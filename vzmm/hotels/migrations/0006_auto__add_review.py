# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'hotels_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hotels.Hotel'], null=True, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('user_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('user_city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('score', self.gf('django.db.models.fields.FloatField')(default=3.0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hotels', ['Review'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'hotels_review')


    models = {
        u'hotels.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email2': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hotels.Hotel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        u'hotels.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'starting_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'hotels.review': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'Review'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hotels.Hotel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {'default': '3.0'}),
            'user_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['hotels']