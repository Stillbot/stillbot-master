# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Boiler'
        db.create_table(u'webapp_boiler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_on', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'webapp', ['Boiler'])

        # Adding model 'Session'
        db.create_table(u'webapp_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('finished_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'webapp', ['Session'])

        # Adding field 'Temperature.sesh'
        db.add_column(u'webapp_temperature', 'sesh',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webapp.Session'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Boiler'
        db.delete_table(u'webapp_boiler')

        # Deleting model 'Session'
        db.delete_table(u'webapp_session')

        # Deleting field 'Temperature.sesh'
        db.delete_column(u'webapp_temperature', 'sesh_id')


    models = {
        u'webapp.boiler': {
            'Meta': {'object_name': 'Boiler'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'webapp.session': {
            'Meta': {'object_name': 'Session'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'finished_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'webapp.temperature': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'Temperature'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sesh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webapp.Session']", 'null': 'True', 'blank': 'True'}),
            'temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'thermistor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'temperatures'", 'to': u"orm['webapp.Thermistor']"})
        },
        u'webapp.thermistor': {
            'Meta': {'object_name': 'Thermistor'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['webapp']