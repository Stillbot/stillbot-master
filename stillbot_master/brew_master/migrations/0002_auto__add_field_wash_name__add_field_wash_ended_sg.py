# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Wash.name'
        db.add_column(u'brew_master_wash', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Wash.ended_sg'
        db.add_column(u'brew_master_wash', 'ended_sg',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Wash.name'
        db.delete_column(u'brew_master_wash', 'name')

        # Deleting field 'Wash.ended_sg'
        db.delete_column(u'brew_master_wash', 'ended_sg')


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
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brew_master.Ingredient']"}),
            'measurement': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'brew_master.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'brew_master.wash': {
            'Meta': {'object_name': 'Wash'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 17, 0, 0)'}),
            'ended_sg': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['brew_master.IngredientMeasurement']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'procedure': ('django.db.models.fields.TextField', [], {}),
            'starting_sg': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        }
    }

    complete_apps = ['brew_master']