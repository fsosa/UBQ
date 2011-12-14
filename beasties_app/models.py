from django.db import models
from django.contrib.auth.models import User

# Declare global variables
MAX_LENGTH = 256 # Maximum length of CharField values

class Nucleotide(models.Model):
    symbol = models.CharField(max_length=1)
    compliment = models.ForeignKey('self', blank=True, null=True)
    
    def __unicode__(self):
        return self.symbol

class Amino_Acid_Name(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    symbol = models.CharField(max_length=MAX_LENGTH)
    
    def __unicode__(self):
        return self.name

# Create your models here.
class Amino_Acid(models.Model):
    name = models.ForeignKey(Amino_Acid_Name)

    nucleotide_1 = models.ForeignKey(Nucleotide, related_name='nucleotide_one')
    nucleotide_2 = models.ForeignKey(Nucleotide, related_name='nucleotide_two')
    nucleotide_3 = models.ForeignKey(Nucleotide, related_name='nucleotide_three')
    
    # Allowd http://stackoverflow.com/questions/395340/can-i-use-a-foreignkey-in-unicode-return
    # def __unicode__(self):
        # return u'%s' % self.id # returns ID...not ideal
        # # return self.name.name # want to return name
        
class Bodypart(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    pretty_name = models.CharField(max_length=MAX_LENGTH)
    
    def __unicode__(self):
        return self.name

class Locked_Nucleotide(models.Model):
    bodypart = models.ForeignKey(Bodypart)
    symbol =  models.ForeignKey(Nucleotide)
    codon_position = models.IntegerField()
    nucleotide_position = models.IntegerField()
    absolute_position = models.IntegerField()
    
    def __unicode__(self):
        return str(self.id)
    
class Weakness(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    pretty_name = models.CharField(max_length=MAX_LENGTH)
    
    def __unicode__(self):
        return self.name
        
class Enemy(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    image_filename = models.CharField(max_length=MAX_LENGTH)  #TODO: Change to ImageField
    group_number = models.IntegerField() #TODO: Possibly same as level.  There are 9 enemeies that share same group number
    
    description = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    weakness_1 = models.ForeignKey(Weakness, related_name='weakness_one', blank=True, null=True)
    weakness_2 = models.ForeignKey(Weakness, related_name='weakness_two', blank=True, null=True)
    weakness_3 = models.ForeignKey(Weakness, related_name='weakness_three', blank=True, null=True)
    weakness_4 = models.ForeignKey(Weakness, related_name='weakness_four', blank=True, null=True)
    
    locked_nucleotide_1 = models.ForeignKey(Locked_Nucleotide, related_name='locked_one', blank=True, null=True)
    locked_nucleotide_2 = models.ForeignKey(Locked_Nucleotide , related_name='locked_two', blank=True, null=True)
    locked_nucleotide_3 = models.ForeignKey(Locked_Nucleotide , related_name='locked_three', blank=True, null=True)
    
    win_message = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    lose_message = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)

    def __unicode__(self):
        return self.name
    
class Game(models.Model):
    code = models.CharField(max_length=MAX_LENGTH)
    name = models.CharField(max_length=MAX_LENGTH)
    #teacher_id = models.ForeignKey(Teachers) #TODO: Create Teacher Group
    status = models.CharField(max_length=MAX_LENGTH, default="active")
    
    def __unicode__(self):
        return self.name
        
class Level(models.Model):
    number = models.IntegerField()
    pretty_name = models.CharField(max_length=MAX_LENGTH)
    num_enemies = models.IntegerField()
    
    def __unicode__(self):
        return self.pretty_name
        

class Phenotype(models.Model):
    bodypart = models.ForeignKey(Bodypart)
    name = models.CharField(max_length=MAX_LENGTH)
    pretty_name = models.CharField(max_length=MAX_LENGTH)
    image_filename = models.CharField(max_length=MAX_LENGTH) #TODO: Change to ImageField
    strong_against = models.ManyToManyField(Weakness, blank=True, null=True)
    
    amino_acid_name_1 = models.ForeignKey(Amino_Acid_Name, related_name='+')
    amino_acid_name_2 = models.ForeignKey(Amino_Acid_Name, related_name='+')
    amino_acid_name_3 = models.ForeignKey(Amino_Acid_Name, related_name='+')
    
    def __unicode__(self):
        return self.name


# TODO: Apply ManyToMany + available_flag, deceaesd_flag, position_num
class User_Enemy(models.Model):
    enemy = models.ForeignKey(Enemy)
    user = models.ForeignKey(User)
    deceased_flag = models.BooleanField() 