from beasties_app.models import *
from django.contrib import admin

class Nucleotide_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['symbol','compliment']})
    ]
    search_fields = ['symbol','compliment']
admin.site.register(Nucleotide, Nucleotide_Admin)

class Amino_Acid_Name_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['name','symbol']}),
    ]
    search_fields = ['name','symbol']
admin.site.register(Amino_Acid_Name, Amino_Acid_Name_Admin)

class Amino_Acid_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['name']}),
    ('Nucleotides', {'fields': ['nucleotide_1','nucleotide_2','nucleotide_3']}),
    ]
    list_display = ('id','name','nucleotide_1','nucleotide_2','nucleotide_3')
    search_fields = ['name']
admin.site.register(Amino_Acid, Amino_Acid_Admin)
    
class Bodypart_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['name','pretty_name']}),
    ]
    list_display = ('pretty_name', 'name')
    search_fields = ['pretty_name']
admin.site.register(Bodypart, Bodypart_Admin)

class Weakness_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['name','pretty_name']}),
    ]
    list_display = ('pretty_name', 'name')
    search_fields = ['pretty_name']
admin.site.register(Weakness, Weakness_Admin)

class Enemy_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['name','image_filename','group_number']}),
    ('Details', {'fields': ['description','weakness']}),
    ('Messages', {'fields': ['win_message','lose_message']}),
    ]
    list_display = ('name','description')
    search_fields = ['name']
admin.site.register(Enemy, Enemy_Admin)

class Game_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['code','name','status']}),
    ]
    list_display = ('code','name','status')
    search_fields = ['code','name','status']
admin.site.register(Game, Game_Admin)

class Level_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['pretty_name','number','num_enemies']}),
    ]
    list_display = ('pretty_name','number','num_enemies')
    search_fields = ['pretty_name','number']
admin.site.register(Level, Level_Admin)

class Player_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['user','game','level','current_enemy']})
    ]
    list_display = ('user','game','level')
    search_fields = ['user','game']
admin.site.register(Player, Player_Admin)

class Zombie_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['player']}),
    ('Bodyparts', {'fields': ['hand_phenotype','horn_phenotype','mouth_phenotype','tail_phenotype']}),
    ('Flags', {'fields': ['built_flag','deceased_flag','won_flag']}),
    ]
    list_display = ('player','built_flag','deceased_flag','won_flag')
    search_fields = ['player']
admin.site.register(Zombie, Zombie_Admin)

class Phenotype_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['name','pretty_name','image_filename','bodypart','strong_against']}),
    #Can't display these amino acids?
    ('Amino Acids', {'fields': ['amino_acid_name_1','amino_acid_name_2','amino_acid_name_3']}),
    ]
    search_fields = ['pretty_name','name','bodypart']
admin.site.register(Phenotype, Phenotype_Admin)

class Player_Enemy_Admin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['enemy','player']}),
    ('Flags', {'fields': ['deceased_flag']}),
    ]
    list_display = ('enemy','player','deceased_flag')
    search_fields = ['enemy','player','deceased_flag']
admin.site.register(Player_Enemy, Player_Enemy_Admin)