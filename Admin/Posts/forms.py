import django_filters
from django import forms

from core.Posts.models import Posts
from core.User.models import User
from core.Utils.filtersets import BaseFilter


class PostsFilter(BaseFilter):
    SEARCH_FIELDS = ['title', 'heading', 'author__email']

    author = django_filters.ModelChoiceFilter(queryset=User.objects.filter(is_active=True).all(),
                                              empty_label='Not selected')

    class Meta:
        model = Posts
        fields = ['author'] + BaseFilter.BASE_FILTER_FIELDS


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=255, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    heading = forms.CharField(label='Heading', max_length=255, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Text', max_length=4048, required=True,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Posts
        fields = ['title', 'heading', 'text']

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)

        if self.author:
            instance.author = self.author

        if commit:
            instance.save()
        return instance
