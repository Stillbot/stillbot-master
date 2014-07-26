# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Thermistor.type'
        db.delete_column(u'webapp_thermistor', 'type')

        # Adding field 'Thermistor.model'
        db.add_column(u'webapp_thermistor', 'model',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Thermistor.type'
        raise RuntimeError("Cannot reverse this migration. 'Thermistor.type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Thermistor.type'
        db.add_column(u'webapp_thermistor', 'type',
                      self.gf('django.db.models.fields.CharField')(max_length=10),
                      keep_default=False)

        # Deleting field 'Thermistor.model'
        db.delete_column(u'webapp_thermistor', 'model')


    models = {
        u'webapp.temperature': {
            'Meta': {'object_name': 'Temperature'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'thermistor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webapp.Thermistor']"})
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