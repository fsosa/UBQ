from django.db import models
from beasties_app.models import Game, Level, Enemy
from django.db.models.signals import post_save
from django.contrib.auth.models import User

MAX_LENGTH = 256 # Maximum length of CharField/CommaSeparatedIntegerField values

class ProxyUser(User):
    class Meta:
        proxy = True
    
    def __unicode__(self):
        if not self.last_name or not self.first_name:
            return u'%s' % (self.username) 
        else:
            return u'%s, %s' % (self.last_name, self.first_name) 

class School(models.Model):
    name = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.name
        

            
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_teacher = models.BooleanField(verbose_name = "Teacher")
    school = models.ForeignKey(School, null=True, blank=True)
    added_by = models.ForeignKey(User, related_name = "userprof_added_by", null=True, blank=True)
    accessible_by = models.ManyToManyField(User, null=True, blank=True, related_name = "userprof_accessible_by")
   
    # Game-specific fields
    game = models.ForeignKey(Game, blank=True, null=True)
    level = models.ForeignKey(Level)
    login_count = models.IntegerField()
    win_count = models.IntegerField()
    loss_count = models.IntegerField()
    defeated_enemies = models.CharField(max_length=MAX_LENGTH, blank=True)
    
    # TODO: Add user-activity related fields (e.g. last-login, etc.)
    
    def __unicode__(self):
        return self.user.username
        
    def save(self, *args, **kwargs):
        """Saves or updates a User Profile"""
        
        print "Trying to save UserProfile"
        
        # Avoid violating the UserProfile unique constraint by checking for previous UserProfiles
        if not self.pk:
            try:
                p = UserProfile.objects.get(user=self.user)
                self.pk = p.pk
                print "Updating UserProfile"
            except UserProfile.DoesNotExist:
                print "UserProfile Not Found"
                pass               
            
        super(UserProfile, self).save(*args, **kwargs)
        
        
    
    
def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        print "Creating new UserProfile"
        profile, new = UserProfile.objects.get_or_create(user=instance)

        
# def update_userprof_accessibility(sender, instance, created, **kwargs):
    # if created: 
        # print instance.accessible_by
        # print instance.user.first_name
        # print request
        # instance.accessible_by.add(instance.user) 
        # instance.save()


class Class(models.Model):
    name = models.CharField(max_length = 80)
    students = models.ManyToManyField(User)
    teacher = models.ForeignKey(ProxyUser, related_name = 'class_teacher')
        
    def __unicode__(self):
        return self.teacher.first_name + ' ' + self.teacher.last_name + '\'s class' 
    
    class Meta:
        verbose_name_plural = 'Classes'       

        

    
post_save.connect(create_user_profile, sender=User)
#post_save.connect(update_userprof_accessibility, sender=UserProfile)