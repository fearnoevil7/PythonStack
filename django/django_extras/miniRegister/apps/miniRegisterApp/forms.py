from django import forms
from . models import User
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
    def clean_password(self):
        password_passed = self.cleaned_data.get('password')
        confirmation_passed = self.cleaned_data.get('confirmation')
        if password_passed != confirmation_passed:
            raise forms.ValidationError("Passwords do not match!!!")
        return password_passed

