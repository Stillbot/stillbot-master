# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Thermistor'
        db.create_table(u'webapp_thermistor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('index', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'webapp', ['Thermistor'])

        # Adding model 'Temperature'
        db.create_table(u'webapp_temperature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('thermistor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webapp.Thermistor'])),
            ('temp', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'webapp', ['Temperature'])


    def backwards(self, orm):
        # Deleting model 'Thermistor'
        db.delete_table(u'webapp_thermistor')

        # Deleting model 'Temperature'
        db.delete_table(u'webapp_temperature')


    models = {
        u'webapp.temperature': {
            'Meta': {'object_name': 'Temperature'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'thermistor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webapp.Thermistor']"})
        },
        u'webapp.thermistor': {
            'Meta': {'object_name': 'Thermistor'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['webapp']