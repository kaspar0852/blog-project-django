from django import forms
from blog.models import *

class PostForm(forms.ModelForm):

    class Meta():
        model  = Post
        #these are the fields we would like to edit
        fields = ('author','title','text')

        #add widgets
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
        #the explanation of the above code is that the text will be connected to 3 css classes
        #-editable medium-editor-textarea postcontent class


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea'})
        }


