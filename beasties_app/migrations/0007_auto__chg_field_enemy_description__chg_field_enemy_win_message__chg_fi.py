# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Enemy.description'
        db.alter_column('beasties_app_enemy', 'description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Enemy.win_message'
        db.alter_column('beasties_app_enemy', 'win_message', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Enemy.lose_message'
        db.alter_column('beasties_app_enemy', 'lose_message', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Enemy.description'
        raise RuntimeError("Cannot reverse this migration. 'Enemy.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Enemy.win_message'
        raise RuntimeError("Cannot reverse this migration. 'Enemy.win_message' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Enemy.lose_message'
        raise RuntimeError("Cannot reverse this migration. 'Enemy.lose_message' and its values cannot be restored.")


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'beasties_app.amino_acid': {
            'Meta': {'object_name': 'Amino_Acid'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Amino_Acid_Name']"}),
            'nucleotide_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Nucleotide']"}),
            'nucleotide_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Nucleotide']"}),
            'nucleotide_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Nucleotide']"})
        },
        'beasties_app.amino_acid_name': {
            'Meta': {'object_name': 'Amino_Acid_Name'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'beasties_app.bodypart': {
            'Meta': {'object_name': 'Bodypart'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pretty_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'beasties_app.enemy': {
            'Meta': {'object_name': 'Enemy'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'group_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_filename': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'lose_message': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'weakness': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['beasties_app.Weakness']", 'symmetrical': 'False'}),
            'win_message': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'beasties_app.game': {
            'Meta': {'object_name': 'Game'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '256'})
        },
        'beasties_app.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_enemies': ('django.db.models.fields.IntegerField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'pretty_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'beasties_app.nucleotide': {
            'Meta': {'object_name': 'Nucleotide'},
            'compliment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Nucleotide']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'beasties_app.phenotype': {
            'Meta': {'object_name': 'Phenotype'},
            'amino_acid_name_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Amino_Acid_Name']"}),
            'amino_acid_name_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Amino_Acid_Name']"}),
            'amino_acid_name_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Amino_Acid_Name']"}),
            'bodypart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Bodypart']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_filename': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pretty_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'strong_against': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['beasties_app.Weakness']", 'null': 'True', 'blank': 'True'})
        },
        'beasties_app.player': {
            'Meta': {'object_name': 'Player'},
            'current_enemy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Enemy']", 'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Level']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'beasties_app.player_enemy': {
            'Meta': {'object_name': 'Player_Enemy'},
            'deceased_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enemy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Enemy']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Player']"})
        },
        'beasties_app.weakness': {
            'Meta': {'object_name': 'Weakness'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pretty_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'beasties_app.zombie': {
            'Meta': {'object_name': 'Zombie'},
            'built_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deceased_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hand_phenotype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Phenotype']"}),
            'horn_phenotype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Phenotype']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mouth_phenotype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Phenotype']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Player']"}),
            'tail_phenotype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['beasties_app.Phenotype']"}),
            'won_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['beasties_app']
