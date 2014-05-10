from django import forms
from story.models import Story

class story_form(forms.ModelForm):
    first_name = forms.CharField(max_length=63, help_text='First Name')
    last_name = forms.CharField(max_length=63, help_text='Last Name')
    title = forms.CharField(max_length=63, help_text='Title')
    story = forms.CharField(widget=forms.Textarea, help_text='Enter your story!')
    class Meta:
        model = Story
        fields = ('first_name', 'last_name', 'title', 'story')