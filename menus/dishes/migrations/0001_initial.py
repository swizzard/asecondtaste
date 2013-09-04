# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MenuItem'
        db.create_table(u'dishes_menuitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dish', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dishes.Dish'], to_field='mk', null=True, unique=True, blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dishes.MenuPage'], to_field='mk', null=True, unique=True, blank=True)),
            ('mk', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'dishes', ['MenuItem'])

        # Adding model 'Menu'
        db.create_table(u'dishes_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mk', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'dishes', ['Menu'])

        # Adding model 'MenuPage'
        db.create_table(u'dishes_menupage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mk', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('menu_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dishes.Menu'], to_field='mk', null=True, unique=True, blank=True)),
        ))
        db.send_create_signal(u'dishes', ['MenuPage'])

        # Adding model 'Dish'
        db.create_table(u'dishes_dish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mk', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dishes.Classification'], null=True, blank=True)),
        ))
        db.send_create_signal(u'dishes', ['Dish'])

        # Adding model 'Classification'
        db.create_table(u'dishes_classification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classification', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'dishes', ['Classification'])


    def backwards(self, orm):
        # Deleting model 'MenuItem'
        db.delete_table(u'dishes_menuitem')

        # Deleting model 'Menu'
        db.delete_table(u'dishes_menu')

        # Deleting model 'MenuPage'
        db.delete_table(u'dishes_menupage')

        # Deleting model 'Dish'
        db.delete_table(u'dishes_dish')

        # Deleting model 'Classification'
        db.delete_table(u'dishes_classification')


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
            'page': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dishes.MenuPage']", 'to_field': "'mk'", 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'dishes.menupage': {
            'Meta': {'object_name': 'MenuPage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_id': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dishes.Menu']", 'to_field': "'mk'", 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'mk': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['dishes']