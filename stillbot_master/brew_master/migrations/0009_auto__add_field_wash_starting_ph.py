# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Wash.starting_ph'
        db.add_column(u'brew_master_wash', 'starting_ph',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Wash.starting_ph'
        db.delete_column(u'brew_master_wash', 'starting_ph')


    models = {
        u'brew_master.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'place_of_origin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brew_master.Place']", 'null': 'True', 'blank': 'True'})
        },
        u'brew_master.ingredientmeasurement': {
            'Meta': {'object_name': 'IngredientMeasurement'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brew_master.Ingredient']"}),
            'measurement': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'brew_master.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'brew_master.wash': {
            'Meta': {'object_name': 'Wash'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 17, 0, 0)'}),
            'ended_sg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['brew_master.IngredientMeasurement']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pitching_temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'procedure': ('django.db.models.fields.TextField', [], {}),
            'starting_ph': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'starting_sg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        },
        u'brew_master.yield': {
            'Meta': {'object_name': 'Yield'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'cut': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'wash': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'yield'", 'null': 'True', 'to': u"orm['brew_master.Wash']"})
        }
    }

    complete_apps = ['brew_master']