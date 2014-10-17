# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Wash'
        db.create_table(u'brew_master_wash', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 17, 0, 0))),
            ('starting_sg', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('procedure', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'brew_master', ['Wash'])

        # Adding M2M table for field ingredients on 'Wash'
        m2m_table_name = db.shorten_name(u'brew_master_wash_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wash', models.ForeignKey(orm[u'brew_master.wash'], null=False)),
            ('ingredientmeasurement', models.ForeignKey(orm[u'brew_master.ingredientmeasurement'], null=False))
        ))
        db.create_unique(m2m_table_name, ['wash_id', 'ingredientmeasurement_id'])

        # Adding model 'IngredientMeasurement'
        db.create_table(u'brew_master_ingredientmeasurement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brew_master.Ingredient'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('measurement', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'brew_master', ['IngredientMeasurement'])

        # Adding model 'Ingredient'
        db.create_table(u'brew_master_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('place_of_origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brew_master.Place'], null=True, blank=True)),
        ))
        db.send_create_signal(u'brew_master', ['Ingredient'])

        # Adding model 'Place'
        db.create_table(u'brew_master_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'brew_master', ['Place'])


    def backwards(self, orm):
        # Deleting model 'Wash'
        db.delete_table(u'brew_master_wash')

        # Removing M2M table for field ingredients on 'Wash'
        db.delete_table(db.shorten_name(u'brew_master_wash_ingredients'))

        # Deleting model 'IngredientMeasurement'
        db.delete_table(u'brew_master_ingredientmeasurement')

        # Deleting model 'Ingredient'
        db.delete_table(u'brew_master_ingredient')

        # Deleting model 'Place'
        db.delete_table(u'brew_master_place')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['brew_master.IngredientMeasurement']", 'null': 'True', 'blank': 'True'}),
            'procedure': ('django.db.models.fields.TextField', [], {}),
            'starting_sg': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        }
    }

    complete_apps = ['brew_master']