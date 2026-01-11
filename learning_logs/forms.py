from django import forms
from .models import Topic, Entry

class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['nome']

class Entryform(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Sua anotação:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}