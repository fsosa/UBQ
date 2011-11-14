from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")

    def save(self, commit=True):
        print "saving custom user..."
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user    
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)
    
class RequiredInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        # get forms that actually have valid data
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                # annoyingly, if a subform is invalid Django explicity raises
                # an AttributeError for cleaned_data
                pass
        if count < 1:
            raise forms.ValidationError('You must fill in at least one field')