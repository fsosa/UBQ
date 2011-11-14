from userprofs.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from userprofs.forms import *

    
class ProfileInline(admin.StackedInline):
    model = UserProfile
    formset = RequiredInlineFormset
    extra = 1
    fk_name = 'user'
    max_num = 1
    can_delete = False
    filter_horizontal = ('accessible_by',)
    exclude = ('added_by',)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "accessible_by":
            kwargs["queryset"] = ProxyUser.objects.filter(userprofile__is_teacher = True).exclude(username = request.user.username)
        return super(ProfileInline, self).formfield_for_manytomany(db_field, request, **kwargs)
        
    
        
class SchoolUserProfInline(admin.TabularInline):
    model = UserProfile
    extra = 3
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = ProxyUser.objects.all()
        return super(SchoolUserProfInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)}
        ),
    )
    inlines = [ProfileInline,]
    
    def save_formset(self, request, form, formset, change):
        print "this got here"
        print formset.model
        
        def set_user(instance):
            print "setting user"   
            instance.added_by = request.user
            instance.save()
            
        if formset.model == UserProfile:
            print "hey this works"
            instances = formset.save(commit=False)
            print instances
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            formset.save()


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    list_filter = ['teacher']
    search_fields =['name']
    filter_horizontal = ('students',)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "students": 
            kwargs["queryset"] = ProxyUser.objects.filter(userprofile__is_teacher = False)
        return super(ClassAdmin, self).formfield_for_manytomany(db_field, request, **kwargs) 
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = ProxyUser.objects.filter(userprofile__is_teacher = True)
        return super(ClassAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class SchoolAdmin(admin.ModelAdmin):
    inlines = [SchoolUserProfInline,]
    



    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(School, SchoolAdmin)
    