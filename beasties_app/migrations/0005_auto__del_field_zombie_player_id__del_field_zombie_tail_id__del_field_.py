# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Zombie.player_id'
        db.delete_column('beasties_app_zombie', 'player_id_id')

        # Deleting field 'Zombie.tail_id'
        db.delete_column('beasties_app_zombie', 'tail_id_id')

        # Deleting field 'Zombie.hand_id'
        db.delete_column('beasties_app_zombie', 'hand_id_id')

        # Deleting field 'Zombie.mouth_id'
        db.delete_column('beasties_app_zombie', 'mouth_id_id')

        # Deleting field 'Zombie.horn_id'
        db.delete_column('beasties_app_zombie', 'horn_id_id')

        # Adding field 'Zombie.player'
        db.add_column('beasties_app_zombie', 'player', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Player']), keep_default=False)

        # Adding field 'Zombie.hand_phenotype'
        db.add_column('beasties_app_zombie', 'hand_phenotype', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Phenotype']), keep_default=False)

        # Adding field 'Zombie.horn_phenotype'
        db.add_column('beasties_app_zombie', 'horn_phenotype', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Phenotype']), keep_default=False)

        # Adding field 'Zombie.mouth_phenotype'
        db.add_column('beasties_app_zombie', 'mouth_phenotype', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Phenotype']), keep_default=False)

        # Adding field 'Zombie.tail_phenotype'
        db.add_column('beasties_app_zombie', 'tail_phenotype', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Phenotype']), keep_default=False)

        # Deleting field 'Phenotype.amino_acid_2_id'
        db.delete_column('beasties_app_phenotype', 'amino_acid_2_id_id')

        # Deleting field 'Phenotype.amino_acid_1_id'
        db.delete_column('beasties_app_phenotype', 'amino_acid_1_id_id')

        # Deleting field 'Phenotype.amino_acid_3_id'
        db.delete_column('beasties_app_phenotype', 'amino_acid_3_id_id')

        # Deleting field 'Phenotype.bodypart_id'
        db.delete_column('beasties_app_phenotype', 'bodypart_id_id')

        # Adding field 'Phenotype.bodypart'
        db.add_column('beasties_app_phenotype', 'bodypart', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Bodypart']), keep_default=False)

        # Adding field 'Phenotype.amino_acid_name_1'
        db.add_column('beasties_app_phenotype', 'amino_acid_name_1', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Amino_Acid_Name']), keep_default=False)

        # Adding field 'Phenotype.amino_acid_name_2'
        db.add_column('beasties_app_phenotype', 'amino_acid_name_2', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Amino_Acid_Name']), keep_default=False)

        # Adding field 'Phenotype.amino_acid_name_3'
        db.add_column('beasties_app_phenotype', 'amino_acid_name_3', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Amino_Acid_Name']), keep_default=False)

        # Removing M2M table for field weakness on 'Phenotype'
        db.delete_table('beasties_app_phenotype_weakness')

        # Adding M2M table for field strong_against on 'Phenotype'
        db.create_table('beasties_app_phenotype_strong_against', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('phenotype', models.ForeignKey(orm['beasties_app.phenotype'], null=False)),
            ('weakness', models.ForeignKey(orm['beasties_app.weakness'], null=False))
        ))
        db.create_unique('beasties_app_phenotype_strong_against', ['phenotype_id', 'weakness_id'])

        # Deleting field 'Player.user_id'
        db.delete_column('beasties_app_player', 'user_id_id')

        # Deleting field 'Player.level_id'
        db.delete_column('beasties_app_player', 'level_id_id')

        # Deleting field 'Player.game_id'
        db.delete_column('beasties_app_player', 'game_id_id')

        # Deleting field 'Player.current_enemy_id'
        db.delete_column('beasties_app_player', 'current_enemy_id_id')

        # Adding field 'Player.user'
        db.add_column('beasties_app_player', 'user', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['auth.User']), keep_default=False)

        # Adding field 'Player.game'
        db.add_column('beasties_app_player', 'game', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Game']), keep_default=False)

        # Adding field 'Player.level'
        db.add_column('beasties_app_player', 'level', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Level']), keep_default=False)

        # Adding field 'Player.current_enemy'
        db.add_column('beasties_app_player', 'current_enemy', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Enemy']), keep_default=False)

        # Deleting field 'Player_Enemy.player_id'
        db.delete_column('beasties_app_player_enemy', 'player_id_id')

        # Deleting field 'Player_Enemy.enemy_id'
        db.delete_column('beasties_app_player_enemy', 'enemy_id_id')

        # Adding field 'Player_Enemy.enemy'
        db.add_column('beasties_app_player_enemy', 'enemy', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Enemy']), keep_default=False)

        # Adding field 'Player_Enemy.player'
        db.add_column('beasties_app_player_enemy', 'player', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Player']), keep_default=False)

        # Adding field 'Nucleotide.compliment'
        db.add_column('beasties_app_nucleotide', 'compliment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beasties_app.Nucleotide'], null=True, blank=True), keep_default=False)

        # Deleting field 'Amino_Acid.nucleotide_2_id'
        db.delete_column('beasties_app_amino_acid', 'nucleotide_2_id_id')

        # Deleting field 'Amino_Acid.nucleotide_1_id'
        db.delete_column('beasties_app_amino_acid', 'nucleotide_1_id_id')

        # Deleting field 'Amino_Acid.version_num'
        db.delete_column('beasties_app_amino_acid', 'version_num')

        # Deleting field 'Amino_Acid.nucleotide_3_id'
        db.delete_column('beasties_app_amino_acid', 'nucleotide_3_id_id')

        # Adding field 'Amino_Acid.nucleotide_1'
        db.add_column('beasties_app_amino_acid', 'nucleotide_1', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Nucleotide']), keep_default=False)

        # Adding field 'Amino_Acid.nucleotide_2'
        db.add_column('beasties_app_amino_acid', 'nucleotide_2', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Nucleotide']), keep_default=False)

        # Adding field 'Amino_Acid.nucleotide_3'
        db.add_column('beasties_app_amino_acid', 'nucleotide_3', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Nucleotide']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Zombie.player_id'
        db.add_column('beasties_app_zombie', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Player']), keep_default=False)

        # Adding field 'Zombie.tail_id'
        db.add_column('beasties_app_zombie', 'tail_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Bodypart']), keep_default=False)

        # Adding field 'Zombie.hand_id'
        db.add_column('beasties_app_zombie', 'hand_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Bodypart']), keep_default=False)

        # Adding field 'Zombie.mouth_id'
        db.add_column('beasties_app_zombie', 'mouth_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Bodypart']), keep_default=False)

        # Adding field 'Zombie.horn_id'
        db.add_column('beasties_app_zombie', 'horn_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Bodypart']), keep_default=False)

        # Deleting field 'Zombie.player'
        db.delete_column('beasties_app_zombie', 'player_id')

        # Deleting field 'Zombie.hand_phenotype'
        db.delete_column('beasties_app_zombie', 'hand_phenotype_id')

        # Deleting field 'Zombie.horn_phenotype'
        db.delete_column('beasties_app_zombie', 'horn_phenotype_id')

        # Deleting field 'Zombie.mouth_phenotype'
        db.delete_column('beasties_app_zombie', 'mouth_phenotype_id')

        # Deleting field 'Zombie.tail_phenotype'
        db.delete_column('beasties_app_zombie', 'tail_phenotype_id')

        # Adding field 'Phenotype.amino_acid_2_id'
        db.add_column('beasties_app_phenotype', 'amino_acid_2_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Amino_Acid']), keep_default=False)

        # Adding field 'Phenotype.amino_acid_1_id'
        db.add_column('beasties_app_phenotype', 'amino_acid_1_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Amino_Acid']), keep_default=False)

        # Adding field 'Phenotype.amino_acid_3_id'
        db.add_column('beasties_app_phenotype', 'amino_acid_3_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Amino_Acid']), keep_default=False)

        # Adding field 'Phenotype.bodypart_id'
        db.add_column('beasties_app_phenotype', 'bodypart_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Bodypart']), keep_default=False)

        # Deleting field 'Phenotype.bodypart'
        db.delete_column('beasties_app_phenotype', 'bodypart_id')

        # Deleting field 'Phenotype.amino_acid_name_1'
        db.delete_column('beasties_app_phenotype', 'amino_acid_name_1_id')

        # Deleting field 'Phenotype.amino_acid_name_2'
        db.delete_column('beasties_app_phenotype', 'amino_acid_name_2_id')

        # Deleting field 'Phenotype.amino_acid_name_3'
        db.delete_column('beasties_app_phenotype', 'amino_acid_name_3_id')

        # Adding M2M table for field weakness on 'Phenotype'
        db.create_table('beasties_app_phenotype_weakness', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('phenotype', models.ForeignKey(orm['beasties_app.phenotype'], null=False)),
            ('weakness', models.ForeignKey(orm['beasties_app.weakness'], null=False))
        ))
        db.create_unique('beasties_app_phenotype_weakness', ['phenotype_id', 'weakness_id'])

        # Removing M2M table for field strong_against on 'Phenotype'
        db.delete_table('beasties_app_phenotype_strong_against')

        # Adding field 'Player.user_id'
        db.add_column('beasties_app_player', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['auth.User']), keep_default=False)

        # Adding field 'Player.level_id'
        db.add_column('beasties_app_player', 'level_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Level']), keep_default=False)

        # Adding field 'Player.game_id'
        db.add_column('beasties_app_player', 'game_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Game']), keep_default=False)

        # Adding field 'Player.current_enemy_id'
        db.add_column('beasties_app_player', 'current_enemy_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Enemy']), keep_default=False)

        # Deleting field 'Player.user'
        db.delete_column('beasties_app_player', 'user_id')

        # Deleting field 'Player.game'
        db.delete_column('beasties_app_player', 'game_id')

        # Deleting field 'Player.level'
        db.delete_column('beasties_app_player', 'level_id')

        # Deleting field 'Player.current_enemy'
        db.delete_column('beasties_app_player', 'current_enemy_id')

        # Adding field 'Player_Enemy.player_id'
        db.add_column('beasties_app_player_enemy', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Player']), keep_default=False)

        # Adding field 'Player_Enemy.enemy_id'
        db.add_column('beasties_app_player_enemy', 'enemy_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['beasties_app.Enemy']), keep_default=False)

        # Deleting field 'Player_Enemy.enemy'
        db.delete_column('beasties_app_player_enemy', 'enemy_id')

        # Deleting field 'Player_Enemy.player'
        db.delete_column('beasties_app_player_enemy', 'player_id')

        # Deleting field 'Nucleotide.compliment'
        db.delete_column('beasties_app_nucleotide', 'compliment_id')

        # Adding field 'Amino_Acid.nucleotide_2_id'
        db.add_column('beasties_app_amino_acid', 'nucleotide_2_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Nucleotide']), keep_default=False)

        # Adding field 'Amino_Acid.nucleotide_1_id'
        db.add_column('beasties_app_amino_acid', 'nucleotide_1_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Nucleotide']), keep_default=False)

        # Adding field 'Amino_Acid.version_num'
        db.add_column('beasties_app_amino_acid', 'version_num', self.gf('django.db.models.fields.IntegerField')(default=''), keep_default=False)

        # Adding field 'Amino_Acid.nucleotide_3_id'
        db.add_column('beasties_app_amino_acid', 'nucleotide_3_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='+', to=orm['beasties_app.Nucleotide']), keep_default=False)

        # Deleting field 'Amino_Acid.nucleotide_1'
        db.delete_column('beasties_app_amino_acid', 'nucleotide_1_id')

        # Deleting field 'Amino_Acid.nucleotide_2'
        db.delete_column('beasties_app_amino_acid', 'nucleotide_2_id')

        # Deleting field 'Amino_Acid.nucleotide_3'
        db.delete_column('beasties_app_amino_acid', 'nucleotide_3_id')


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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'group_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_filename': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'lose_message': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'weakness': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['beasties_app.Weakness']", 'symmetrical': 'False'}),
            'win_message': ('django.db.models.fields.CharField', [], {'max_length': '256'})
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
            'strong_against': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['beasties_app.Weakness']", 'symmetrical': 'False'})
        },
        'beasties_app.player': {
            'Meta': {'object_name': 'Player'},
            'current_enemy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beasties_app.Enemy']"}),
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
