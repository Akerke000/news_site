from django import forms
from .models import Post

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFieleField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput)
        kwargs.setdefault('required', False)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial = None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class Postform(forms.ModelForm):
    images  = MultipleFieleField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'images')
    