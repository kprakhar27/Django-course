from django import forms

from main import models


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=256)
    about_me = forms.CharField(widget=forms.Textarea())
    active = forms.BooleanField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'
