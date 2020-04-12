from django import forms
from .models import Course, Description, Comment
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class DescriptionForm(forms.Form):
    description = forms.CharField(max_length=1000)

class AddComment(forms.Form):
    model = Comment
    fields = "__all__"
