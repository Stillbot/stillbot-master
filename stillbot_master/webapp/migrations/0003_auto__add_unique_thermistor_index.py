# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Thermistor', fields ['index']
        db.create_unique(u'webapp_thermistor', ['index'])


    def backwards(self, orm):
        # Removing unique constraint on 'Thermistor', fields ['index']
        db.delete_unique(u'webapp_thermistor', ['index'])


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['webapp']