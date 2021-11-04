from .models import Forum
from django import forms

class forumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['ForumTitle', 'ForumFrom','ForumMessage']

    input_attrs_title = {
        'type' : 'text',
        'placeholder' : 'Judul Pesan Cerita',
        'class' : 'attrs-title',
    }

    input_attrs_from = {
        'type' : 'text',
        'placeholder' : 'Nama Penulis', 
        'class' : 'attrs-from',
    }

    input_attrs_message = {
        'type' : 'text',
        'placeholder' : 'Pesan Cerita...',
        'class' : 'attrs-message',
    }

    ForumTitle = forms.CharField(label='JUDUL', required=True, max_length=15, 
    widget= forms.TextInput(attrs=input_attrs_title))

    ForumFrom = forms.CharField(label='PENULIS', required=True, max_length=20, 
    widget= forms.TextInput(attrs=input_attrs_from))

    ForumMessage = forms.CharField(label='PESAN CERITA', required=True, max_length=350, 
    widget= forms.Textarea(attrs=input_attrs_message))