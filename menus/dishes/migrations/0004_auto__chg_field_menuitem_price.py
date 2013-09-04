# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MenuItem.price'
        db.alter_column(u'dishes_menuitem', 'price', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

    def backwards(self, orm):

        # Changing field 'MenuItem.price'
        db.alter_column(u'dishes_menuitem', 'price', self.gf('django.db.models.fields.CharField')(default='', max_length=5))

    models = {
        u'dishes.classification': {
            'Meta': {'object_name': 'Classification'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dishes.dish': {
            'Meta': {'object_name': 'Dish'},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dishes.Classification']", 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mk': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'dishes.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mk': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'restaurant': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'dishes.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'dish': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dishes.Dish']", 'to_field': "'mk'", 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mk': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dishes.MenuPage']", 'to_field': "'mk'", 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'dishes.menupage': {
            'Meta': {'object_name': 'MenuPage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dishes.Menu']", 'to_field': "'mk'", 'null': 'True', 'blank': 'True'}),
            'mk': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['dishes']